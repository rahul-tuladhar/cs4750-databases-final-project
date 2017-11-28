from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User, Group, Permission
from django.template.context_processors import csrf
from django.template import RequestContext
from django.utils import timezone
from django.db.models import Q
from django.utils import timezone
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, resolve_url
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail

import json
import datetime
import random
import hashlib

from data.models import Customer
from .forms import RegistrationForm
from .forms import UserForm


# Create your views here.
from data.models import Customer
from .forms import RegistrationForm



def user_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            up = Customer.objects.get(id = user.id)
        else:
             return HttpResponse("Invalid login information. (If you believe you have entered the correct login information, contact the Site Manager.)")
    else:
        return render(request, 'user/login.html', {})

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data['email']
            # user_type = form.cleaned_data['user_type']

            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = timezone.now() + datetime.timedelta(2)

            customer = User.objects.get(username=username)

            customer_profile = Customer(id=customer.id, customer=customer, activation_key=activation_key,
                   key_expires=key_expires)
            customer_profile.save()

            email_subject = 'Vapor Registration Confirmation'

            email_message = "Thank you for signing up with Vapor! To activate your account, please visit: \
                http://127.0.0.1:8000/users/login/"

            send_mail(email_subject, email_message, 'rt4hc@gmail.com', [email], fail_silently=False)

            customer = authenticate(username=username, password=raw_password)
            login(request, customer)
            return redirect('/newuserkeylanding/')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def register_confirm(request, activation_key):
    if request.user.is_authenticated():
        HttpResponseRedirect('http://127.0.0.1:8000/')

    customer_profile = get_object_or_404(Customer, activation_key=activation_key)

    if customer_profile.key_expires < timezone.now():
        return HttpResponse("Activation key not working! Please register a new account.")

    customer = customer_profile.customer
    customer.is_active = True
    customer.save()
    return HttpResponse("Registration successful! Please go to the login page to log in to your account!")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user/login/')




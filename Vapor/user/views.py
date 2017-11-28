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
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, resolve_url
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
# Create your views here.
from data.models import Customers

def user_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            up = UserProfile.objects.get(id = user.id)
            if up.suspended:
                return HttpResponse("Your account has been suspended. Contact a site manager for more information.")
            else:
                login(request, user)
                return HttpResponseRedirect('/')
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
            user_type = form.cleaned_data['user_type']

            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = timezone.now() + datetime.timedelta(2)

            user = User.objects.get(username=username)

            user_profile = UserProfile(id=user.id, user=user, activation_key=activation_key,
                   key_expires=key_expires, user_type=user_type)
            user_profile.save()

            email_subject = 'Vapor Registration Confirmation'

            email_message = "Thank you for signing up with Vapor! To activate your account, please visit: \
                http://127.0.0.1:8000/users/login/"

            send_mail(email_subject, email_message, 'rt4hc@gmail.com', [email], fail_silently=False)

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/newuserkeylanding/')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def register_confirm(request, activation_key):
    if request.user.is_authenticated():
        HttpResponseRedirect('http://127.0.0.1:8000/')

    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    if user_profile.key_expires < timezone.now():
        return HttpResponse("Activation key not working! Please register a new account.")

    user = user_profile.user
    user.is_active = True
    user.save()
    return HttpResponse("Registration successful! Please go to the login page to log in to your account!")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user/login/')




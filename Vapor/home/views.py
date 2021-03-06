from django.shortcuts import render
from data.models import Customer as User


def homepage(request):
	context = {'is_logged_in': False}
	if request.user.is_authenticated():
		context = {'is_logged_in': True}
	return render(request, 'home/home.html', context)

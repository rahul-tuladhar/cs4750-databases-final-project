from django.shortcuts import render

# Create your views here.

def defaultCart(request):
	context = {}
	return render(request, 'cart/defaultcart.html', context)
from django.shortcuts import render

# Create your views here.

def defaultView(request):
	context = {}
	return render(request, 'search/defaultview.html', context)
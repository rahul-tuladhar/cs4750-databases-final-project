from django.shortcuts import render, redirect
from data.models import Products, Merchants, Developers

# Create your views here.

def search_view(request):
	context = {}

	if request.method == "POST":
		if request.POST.get('search_button'):
			name_search = request.POST.get('name_search')
			price_mod = request.POST.get('price_mod')
			price_search = request.POST.get('price_search')
			genre_search = request.POST.get('genre_search')
			merch_search = request.POST.get('merch_search')
			dev_search = request.POST.get('dev_search')

		qset = Products.objects.all()
		if name_search:
			qset = qset.filter(product_name=name_search)
		if price_mod and price_search:
			if price_mod == 'less':
				qset = qset.filter(price__lt=price_search)
			elif price_mod == 'greater':
				qset = qset.filter(price__gt=price_search)
			else:
				qset = qset.filter(price=price_search)
		if genre_search:
			qset = qset.filter(genre=genre_search)
		if merch_search:
			try:
				merch = Merchants.objects.get(merchant_name=merch_search)
				qset = qset.filter(merchant_id=merch)
			except:
				print("merchant not found")
		if dev_search:
			try:
				dev = Developers.objects.get(developer_name=dev_search)
				qset = qset.filter(developer_id=dev)
			except:
				print("developer not found")

		data = []
		for item in qset:
			data.append(item)

		request.session['search_results'] = data

		return redirect('/search/results')

	return render(request, 'search/searchview.html', context)

def results_view(request):
	data = request.session['search_results']
	context = {'results': data}


	return render(request, 'search/resultsview.html', context)

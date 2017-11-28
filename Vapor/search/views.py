from django.shortcuts import render, redirect
from data.models import Product, Merchant, Developer, Customer, ShoppingCart, Review
from .forms import AddToCartForm

# Create your views here.

def detail_view(request, product_id):
	context = {}
	product = Product.objects.get(id=product_id)
	context['product'] = product

	reviews = Review.objects.filter(product_id=product_id)
	context['reviews'] = reviews
	print(reviews)

	# for when user clicks 'add to cart'
	if request.method == "POST":
		form = AddToCartForm(request.POST)
		if request.POST.get('add_cart'):
			if form.is_valid():
				cform = form.cleaned_data
				customer = cform['customer']

				sc = ShoppingCart(product_id=product, customer_id=customer)
				sc.save()
				return redirect('/cart/'+str(customer.id))

	else:
		form = AddToCartForm()

	context['form'] = form


	return render(request, 'search/detailview.html', context)

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

		qset = Product.objects.all()
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
				merch = Merchant.objects.get(merchant_name=merch_search)
				qset = qset.filter(merchant_id=merch)
			except:
				print("merchant not found")
		if dev_search:
			try:
				dev = Developer.objects.get(developer_name=dev_search)
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
	print("render results")
	data = request.session['search_results']
	context = {'results': data}

	if request.method == "POST":
		view_prod_id = request.POST.get('prod_id')

		return redirect('/search/product/' + view_prod_id)

	return render(request, 'search/resultsview.html', context)

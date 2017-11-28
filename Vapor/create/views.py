from django.shortcuts import render
from .forms import NewProductForm
from data.models import Product

# Create your views here.

def product_view(request):
	if request.method == 'POST':
		form = NewProductForm(request.POST)
		if form.is_valid():
			cform = form.cleaned_data
			print(cform)
			new_product = Product(product_name=cform['product_name'], product_description=cform['product_desc'], price=cform['price'])
			new_product.save()
	else:
		form = NewProductForm()
	context = {'form': form}
	return render(request, 'create/newProduct.html', context)
from django.shortcuts import render, redirect
from .forms import NewProductForm
from data.models import Product

# Create your views here.

def product_view(request):
	if request.method == 'POST':
		form = NewProductForm(request.POST)
		print("errors in create/views.py")
		print(form.errors)
		print(form.non_field_errors)
		if form.is_valid():
			cform = form.cleaned_data
			print(cform)
			new_product = Product(product_name=cform['product_name'], product_description=cform['product_desc'], price=cform['price'], genre=cform['genre'], release_date=cform['release_date'], stock=cform['stock'], merchant_id=cform['merchant_id'], developer_id=cform['developer_id'])
			new_product.save()

			return redirect('/search/product/' + str(new_product.id))
	else:
		form = NewProductForm()
	context = {'form': form, 'is_logged_in': True}
	return render(request, 'create/newProduct.html', context)
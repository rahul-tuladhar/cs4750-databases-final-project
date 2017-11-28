from django.shortcuts import render
from data.models import Customers, ShoppingCart, Products


# Create your views here.

def cart_view(request, user_id):
	context = {'name': "Null", 'items': []}

	# Get the customer for this cart
	customer = Customers.objects.get(id=user_id)

	# If the customer is valid, add name to context['name'] and add items in his cart to context['items']
	if customer:
		context['name'] = customer.customer_name
		list_item_ids = ShoppingCart.objects.filter(customer_id=user_id)
		list_items = []
		for item in list_item_ids:
			product = item.product_id
			list_items.append(product)
		context['items'] = list_items



	return render(request, 'cart/cart_view.html', context)
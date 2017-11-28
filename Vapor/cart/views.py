from django.shortcuts import render, redirect
from data.models import Customer, ShoppingCart, Product, Transaction
import datetime
from decimal import *


# Create your views here.

def cart_view(request):
	user_id = request.user.id
	context = {'name': '', 'items': []}

	# Get the customer for this cart
	try: 
		customer = Customer.objects.get(id=1)
	except:
		customer = None

	print(customer)

	# If the customer is valid, add name to context['name'] and add items in his cart to context['items']
	if customer:
		context['name'] = customer.customer_name
		list_item_ids = ShoppingCart.objects.filter(customer_id=user_id)
		list_items = []
		transaction_total = 0

		for item in list_item_ids:
			product = item.product_id
			list_items.append(product)
			transaction_total += float(product.price)

		context['items'] = list_items
		context['transaction_total'] = Decimal(transaction_total).quantize(Decimal('.01'))
		context['is_logged_in'] = True

	if request.method == 'POST':
		if request.POST.get('checkout'):
			dt = datetime.datetime.now()
			payment_method = "bitcoins"
			for item in list_item_ids:
				merchant = item.product_id.merchant_id
				prod = item.product_id

				# One transaction for each item in the cart
				transac = Transaction(date_time=dt, 
										amount_paid=transaction_total, 
										payment_method=payment_method,
										customer_id=customer,
										merchant_id=merchant,
										product_id=prod)
				transac.save()

			# Delete the items from the shoppping cart
			ShoppingCart.objects.filter(customer_id=customer).delete()

			return redirect('/home')



	return render(request, 'cart/cart_view.html', context)
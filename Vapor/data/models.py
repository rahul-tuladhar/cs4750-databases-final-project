from django.db import models
from django import forms
from django.contrib.auth.models import User, Group

class Customer(models.Model):
    # Attributes of the report model
    '''CREATE TABLE customers (
            customer_id int AUTO_INCREMENT,
            customer_name varchar(100),
            street_address varchar(100),
            city varchar(50),
            state varchar(20),
            zip int,
            phone_number varMchar(20),
            cc_number int,
            cc_exp_date datetime,
            cc_security_code varchar(10),
            PRIMARY KEY(customer_id)
            )'''
    
    #customer = models.OneToOneField(User)
    #activation_key = models.CharField(max_length = 200)
    customer_name = models.TextField(max_length = 400) # only one document can have document=true field
    street_address = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length = 100, default="")
    zip = models.CharField(max_length = 100, null = True)
    # company_name = models.ForeignKey('Company', on_delete=models.SET_NULL, null = true)
    cc_number = models.CharField(max_length = 200)
    cc_exp_date = models.BooleanField(default = False)
    cc_security_code = models.CharField(max_length = 200)

    def __str__(self):
        # Should probably have each object be able to return a string of itself
        return self.customer_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular report instance.
        """
        return (id)

class Merchant(models.Model):
    # Attributes of the report model
    '''CREATE TABLE merchants (
            merchant_id int AUTO_INCREMENT,
            merchant_name vaMrchar(100),
            street_address varchar(100),
            city varchar(50),
            state varchar(20),
            zip int,
            phone_number varchar(20),
            
            PRIMARY KEY(merchant_id)
            )'''
    
    merchant_name = models.CharField(max_length = 400) # only one document can have document=true field
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length = 100, default="")
    state = models.CharField(max_length = 100, null = True)
    zip = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length=20, default = False)

    def __str__(self):
        # Should probably have each object be able to return a string of itself
        return self.merchant_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular report instance.
        """
        return (id)

class Developer(models.Model):
    # Attributes of the report model
    '''CREATE TABLE developers (
			developer_id int AUTO_INCREMENT,
			developer_name varchar(100),
			street_address varchar(100),
			city varchar(50),
			state varchar(20),
			zip int,
			phone_number varchar(20),
			PRIMARY KEY(developer_id)
			)'''

   
    developer_name = models.CharField(max_length = 400) # only one document can have document=true field
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length = 100, default="")
    state = models.CharField(max_length = 100, null = True)
    zip = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length=20, default = False)

    def __str__(self):
        # Should probably have each object be able to return a string of itself
        return self.developer_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular report instance.
        """
        return (id)

class Product(models.Model):
    '''CREATE TABLE products (
			product_id int AUTO_INCREMENT,
			product_name varchar(100),
			product_description varchar(400),
			price decimal(20, 2),
			genre varchar(100),
			release_date datetime,
			stock int,
			merchant_id int,
			developer_id int,
			PRIMARY KEY(product_id),
			FOREIGN KEY(merchant_id) references merchants(merchant_id),
			FOREIGN KEY(developer_id) references developers(developer_id)
			)'''

    
    product_name = models.CharField(max_length = 400) # only one document can have document=true field
    product_description = models.CharField(max_length=200)
    price = models.CharField(max_length = 100, default="")
    genre = models.CharField(max_length = 100, null = True)
    release_date = models.DateTimeField(max_length = 200)
    stock = models.BigIntegerField()
    merchant_id = models.ForeignKey(Merchant, on_delete = models.CASCADE)
    developer_id = models.ForeignKey(Developer, on_delete = models.CASCADE)

    def __str__(self):
        # Should probably have each object be able to return a string of itself
        return self.product_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular report instance.
        """
        return (id)

class ShoppingCart(models.Model):
    '''CREATE TABLE shopping_cart (
			customer_id int,
			product_id int,
			PRIMARY KEY(customer_id, product_id),
			FOREIGN KEY(customer_id) references customers(customer_id),
			FOREIGN KEY(product_id) references products(product_id)
			)'''

    product_id = models.ForeignKey(Product, on_delete = models.CASCADE) # only one document can have document=true field
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)

    def __str__(self):
        # Should probably have each object be able to return a string of itself
        return "customer {} wants item {}".format(self.customer_id, self.product_id)

    def get_absolute_url(self):
        """
        Returns the url to access a particular report instance.
        """
        return ("shopping_cart/"+id)



class Transaction(models.Model):
    '''CREATE TABLE transactions (
			transaction_id int AUTO_INCREMENT,
			date_time datetime,
			amount_paid decimal(20,2),
			payment_method varchar(20),
			customer_id int,
			merchant_id int,
			product_id int,
			PRIMARY KEY(transaction_id),
			FOREIGN KEY(customer_id) references customers(customer_id),
			FOREIGN KEY(merchant_id) references merchants(merchant_id),
			FOREIGN KEY(product_id) references products(product_id)
			)'''

    date_time = models.DateTimeField(auto_now_add = True)
    amount_paid = models.DecimalField(decimal_places = 2, max_digits=50)
    payment_method = models.CharField(max_length = 40)
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    merchant_id = models.ForeignKey(Merchant, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE) # only one document can have document=true field
   

    def __str__(self):
        # Should probably have each object be able to return a string of itself
        return self.id

    def get_absolute_url(self):
        """
        Returns the url to access a particular report instance.
        """
        return ("transaction_id/"+id)

class Review(models.Model):
    '''CREATE TABLE reviews (
			review_id int AUTO_INCREMENT,
			review_content varchar(1000),
			review_date_time datetime,
			review_rating int,
			customer_id int,
			product_id int,
			PRIMARY KEY(review_id),
			FOREIGN KEY(customer_id) references customers(customer_id),
			FOREIGN KEY(product_id) references products(product_id)
			)'''

    
    review_content = models.TextField(max_length = 500)
    review_date_time = models.DateTimeField(auto_now_add = True)
    reivew_rating = models.DecimalField(decimal_places=1, max_digits=3, max_length = 40)
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    merchant_id = models.ForeignKey(Merchant, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE) # only one document can have document=true field
   

    def __str__(self):
        # Should probably have each object be able to return a string of itself
        return str(self.review_content)

    def get_absolute_url(self):
        """
        Returns the url to access a particular report instance.
        """
        return ("reviews_id/"+id)

class DeveloperProducesProduct(models.Model):
    ''''CREATE TABLE developer_produces_product (
			product_id int,
			developer_id int,
			PRIMARY KEY(product_id, developer_id),
			FOREIGN KEY(product_id) references products(product_id),
			FOREIGN KEY(developer_id) references developers(developer_id)
			)'''

    
    developer_id = models.ForeignKey(Developer, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE) # only one document can have document=true field
   

    def __str__(self):
        # Should probably have each object be able to return a string of itself
        return self.id

    def get_absolute_url(self):
        """
        Returns the url to access a particular report instance.
        """
        return ("dpp/"+id)

class SupportTicket(models.Model):
    '''CREATE TABLE support_tickets (
			ticket_id int AUTO_INCREMENT,
			ticket_content varchar(1000),
			ticket_date_time datetime,
			customer_id int,
			PRIMARY KEY(ticket_id),
			FOREIGN KEY(customer_id) references customers(customer_id)
			)'''

    
    ticket_content = models.TextField(max_length = 500)
    ticket_date_time = models.DateTimeField(auto_now_add = True) # only one document can have document=true field
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        # Should probably have each object be able to return a string of itself
        return self.id

    def get_absolute_url(self):
        """
        Returns the url to access a particular report instance.
        """
        return ("support_tickets/"+id)
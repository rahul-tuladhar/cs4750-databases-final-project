from django import forms
from data.models import Merchant, Developer

class NewProductForm(forms.Form):
	product_name = forms.CharField(label="Product Name", widget=forms.TextInput(attrs={'size': 40, 'class':'form-control'}))
	product_desc = forms.CharField(label="Product Description", widget=forms.TextInput(attrs={'class':'form-control'}))
	price = forms.CharField(label="Price", widget=forms.TextInput(attrs={'class':'form-control'}))
	genre = forms.CharField(label="Genre", widget=forms.TextInput(attrs={'class':'form-control'}))
	release_date = forms.DateTimeField(label="Release Date", widget=forms.TextInput(attrs={'class':'form-control'}))
	stock = forms.IntegerField(label="In Stock", widget=forms.TextInput(attrs={'class':'form-control'}))
	merchant_id = forms.ModelChoiceField(queryset=Merchant.objects.all(), empty_label="Merchant")
	developer_id = forms.ModelChoiceField(queryset=Developer.objects.all(), empty_label="Developer")
	

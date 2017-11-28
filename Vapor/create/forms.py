from django import forms

class NewProductForm(forms.Form):
	product_name = forms.CharField(label="Product Name", widget=forms.TextInput(attrs={'class':'form-control'}))
	product_desc = forms.CharField(label="Product Description", widget=forms.TextInput(attrs={'class':'form-control'}))
	price = forms.CharField(label="Price", widget=forms.TextInput(attrs={'class':'form-control'}))

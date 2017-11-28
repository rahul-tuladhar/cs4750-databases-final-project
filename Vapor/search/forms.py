from django import forms
from data.models import Customer

class AddToCartForm(forms.Form):
	customer = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label="Who are you?")
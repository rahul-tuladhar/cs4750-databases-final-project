from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.template.context_processors import csrf
from django.forms.models import inlineformset_factory

# CATEGORIES = (
#     ('Investor User', 'Investor User'),
#     ('Company User', 'Company User'),
# )

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,)
    last_name = forms.CharField(max_length=30,)
    email = forms.EmailField(max_length=254, help_text='Please enter a valid email address.')
    user_type = forms.ChoiceField(choices=CATEGORIES, help_text='Please indicate if you are an Investor or Company User.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

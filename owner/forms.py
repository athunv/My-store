from django import forms
from django.contrib.auth.models import User
from api.models import product

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()

class Registrationform(forms.ModelForm):
    
    class Meta:

        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]

class Productform(forms.ModelForm):

    class Meta:

        model = product
        fields = '__all__'
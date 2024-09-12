from .models import *
from django import forms


class AddAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']


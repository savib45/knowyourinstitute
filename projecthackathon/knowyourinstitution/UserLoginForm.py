from django.forms import ModelForm
from .models import  User
from django import forms

class UserLoginFormModel(ModelForm):

    class Meta:
        model = User

        fields = ['username','password']
        widgets={
            'password': forms.TextInput(attrs={ 'type':'password' })
            }


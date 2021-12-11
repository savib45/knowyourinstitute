from django.forms import ModelForm
from .models import  UserProfile
from django.contrib.auth.models import User
from django import forms

class UserProfileFormModel(ModelForm):
    class Meta:
        model = UserProfile
        fields  = ['contactNumber','userCollegeName']

class UserFormModel(ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
from django.forms import ModelForm
from .models import  User

class UserLoginFormModel(ModelForm):

    class Meta:
        model = User

        fields = ['username','password']


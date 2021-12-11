from django.forms import ModelForm
from .models import Review

class RatingForm(ModelForm):


    class Meta:
        model = Review
        fields = ['text','rating']

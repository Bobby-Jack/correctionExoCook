from django import forms
from .models import Ingredient

class Ingredient_form(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


from django.shortcuts import render, redirect
from .models import Ingredient
from .form import *
# Create your views here.

def getHome(request):
    ings = Ingredient.objects.all()
    return render(request, 'cook/ingredient/home.html', {"ings": ings})

def createIngredient(request):
    if request.method == 'POST':
        form = Ingredient_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Ingredient_form()
    return render(request, 'cook/ingredient/createIngredient.html', {"form": form})


def getIngredientById(request, id):
    ing = Ingredient.objects.get(id=id)
    return render (request , 'cook/ingredient/detail.html', {"ing": ing})
    
def destroyIngredient(request, id):
    ing = Ingredient(id)
    ing.delete()
    return redirect('home')
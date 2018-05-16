from django.shortcuts import render
from .models import Ingredient, Food, Meal
def home(request):
    ingredients = Ingredient.objects
    foods = Food.objects
    meals = Meal.objects
    return render(request, 'daycal/home.html', {'foods':foods, 'meals':meals,'ingredients':ingredients})
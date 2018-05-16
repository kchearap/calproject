from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Ingredient, Food, Meal
from datetime import datetime

def home(request):
    User = get_user_model()
    ingredients = Ingredient.objects
    foods = Food.objects
    if request.user.is_authenticated:
        meals = Meal.objects.filter(user=request.user)
    else:    
        meals = None
    return render(request, 'daycal/home.html', {'foods':foods,'meals':meals})

def addmeal(request):
    User = get_user_model()
    meal = Meal.objects.filter(user=request.user,create_time=datetime.strptime(request.POST['eat_date'], "%d/%m/%Y").date())
    if meal.count() == 0:	
        meal=Meal(user=request.user, create_time=datetime.strptime(request.POST['eat_date'], "%d/%m/%Y").date())
        meal.save()
    selected_values = request.POST.getlist('select')
    for selected in selected_values:
        meal.foods.add(selected)
    meal.save()
    ingredients = Ingredient.objects
    foods = Food.objects
    if request.user.is_authenticated:
        meals = Meal.objects.filter(user=request.user)
    else:    
        meals = None    
    return render(request, 'daycal/addmeal.html', {'foods':foods,'meals':meals})

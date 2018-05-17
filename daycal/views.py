from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Ingredient, Food, Meal
from datetime import datetime

def home(request):
    User = get_user_model()
    ingredients = Ingredient.objects
    foods = Food.objects
    search_term=''
    if 'search_box' in request.GET:
        search_term = request.GET['search_box']
        foods = foods.filter(name__icontains=search_term)
    
    if request.user.is_authenticated:
        meals = Meal.objects.filter(user=request.user).order_by('-create_time')
    else:    
        meals = None
    return render(request, 'daycal/home.html', {'foods':foods,'meals':meals})

def addmeal(request):
    print (request.POST)
    User = get_user_model()
    meal = Meal.objects.filter(user=request.user,create_time=datetime.strptime(request.POST['eat_date'], "%d/%m/%Y").date())
    if meal.count() == 0:
        meal=Meal(user=request.user, create_time=datetime.strptime(request.POST['eat_date'], "%d/%m/%Y").date())
        meal.save()
        selected_values = request.POST.getlist('select')
        for selected in selected_values:
            meal.foods.add(selected)
        meal.save()
    else:
        for meal_selected in meal:
            selected_values = request.POST.getlist('select')
            for selected in selected_values:
                meal_selected.foods.add(selected)
            meal_selected.save()
    ingredients = Ingredient.objects
    foods = Food.objects
    if request.user.is_authenticated:
        meals = Meal.objects.filter(user=request.user).order_by('-create_time')
    else:
        meals = None
    return render(request, 'daycal/addmeal.html', {'values':selected_values})

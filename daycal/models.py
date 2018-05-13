from django.db import models
from datetime import date
from django.conf import settings
from django.contrib.auth import get_user_model

class Ingredient(models.Model):
    name = models.CharField(blank=False, max_length=255)
    
    def __str__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField(blank=False, max_length=255)
    ingradients = models.ManyToManyField(Ingredient)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateField(default=date.today)
    foods = models.ManyToManyField(Food)
    
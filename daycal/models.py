from django.db import models
from datetime import date
from django.conf import settings
from django.contrib.auth import get_user_model

class Ingredient(models.Model):
    name = models.CharField(blank=False, max_length=255,primary_key=True)
    
    def __str__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField(blank=False, max_length=255)
    ingredients = models.ManyToManyField(Ingredient,related_name='ingredients')
    image = models.ImageField(upload_to='images/')
    calorie = models.SmallIntegerField(null=True,default=2000)

    def __str__(self):
        return self.name
    
class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateField(default=date.today)
    foods = models.ManyToManyField(Food)
    cal_per_day = models.SmallIntegerField(null=True,default=2000)
    
    def calculate_cal(self):
        return sum(food.calorie for food in self.foods.all())
    
    def save(self, *args, **kwargs):
        self.cal_per_day = self.calculate_cal()      
        super().save(*args, **kwargs)  # Call the "real" save() method.
from django.db import models
from datetime import date
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )    
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)
    birth_date = models.DateField(default=date.today)
    sex = models.CharField(max_length=1, choices=SEX)
    height = models.SmallIntegerField(null=True)
    weight = models.SmallIntegerField(null=True)
    bmi = models.DecimalField(null=True,max_digits=7,decimal_places=2)
    cal_per_day = models.SmallIntegerField(null=True,default=2000)
    REQUIRED_FIELDS = ['email','birth_date', 'height','weight','sex','cal_per_day']
    
    def __str__(self):
        return self.name 
    
    def age(self):
        today = date.today()

        try: 
            birthday = self.birth_date.replace(year=today.year)
        # raised when birth date is February 29 and the current year is not a leap year
        except ValueError:
            birthday = self.birth_date.replace(year=today.year, day=self.birth_date.day-1)

        if birthday > today:
            return today.year - self.birth_date.year - 1
        else:
            return today.year - self.birth_date.year       
    
    def save(self, *args, **kwargs):
        self.bmi = self.weight / (self.height/100) ** 2
        self.cal_per_day = 10 * int(self.weight) + 6.25 * int(self.height) - 5 * self.age() + 5
        super().save(*args, **kwargs)  # Call the "real" save() method.

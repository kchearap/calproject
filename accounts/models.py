from django.db import models
from datetime import date
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from .validators import validate_Height,validate_Weight,validate_BirthDate,validate_Sex
class CustomUser(AbstractUser):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    # First/last name is not a global-friendly pattern
    birth_date = models.DateField(default=date.today,validators=[validate_BirthDate])
    sex = models.CharField(max_length=1, choices=SEX,validators=[validate_Sex])
    height = models.DecimalField(null=True,max_digits=7,decimal_places=1,validators=[validate_Height])
    weight = models.DecimalField(null=True,max_digits=7,decimal_places=2,validators=[validate_Weight])
    bmi = models.DecimalField(null=True,max_digits=7,decimal_places=2)
    cal_per_day = models.SmallIntegerField(null=True,default=2000)
    REQUIRED_FIELDS = ['email','birth_date', 'height','weight','sex']

    def __str__(self):
        return self.username

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
        try:
            self.full_clean()
            self.bmi = self.weight / (self.height/100) ** 2
            if self.sex == 'M':
                self.cal_per_day = round((10 * float(self.weight)) + (6.25 * float(self.height)) - (5 * self.age()) + 5)
            else:
                self.cal_per_day = round((10 * float(self.weight)) + (6.25 * float(self.height)) - (5 * self.age()) - 161)
            super().save(*args, **kwargs)  # Call the "real" save() method.
        except ValidationError:
            raise ValidationError(_,"Sorry, Field Enter is invalid. ")

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import date

def validate_Height(value):
    if value < 100:
        raise ValidationError(_,"Sorry, the height submitted is invalid. The Minimum Height Allow is 100.")

def validate_Weight(value):
    if value < 20:
        raise ValidationError(_,"Sorry, the weight submitted is invalid. The Minimum Weight Allow is 20.")

def validate_BirthDate(value):
    if value >= date.today():
        raise ValidationError(_,"Sorry, the birth date submitted is invalid. ")


def validate_Sex(value):
    if value not in {"M","F"}:
        raise ValidationError(_,"Sorry, the birth date submitted is invalid. ")

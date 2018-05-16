from django.urls import path, include
from . import views

urlpatterns = [
    path('addmeal', views.addmeal, name='addmeal'),
]

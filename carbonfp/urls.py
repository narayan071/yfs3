from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.calculate_carbon_footprint, name='calculate_carbon_footprint'),
]

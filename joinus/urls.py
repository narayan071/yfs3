from django.urls import path
from . import views

urlpatterns = [
    path("", views.joinus, name="joinus"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("chapters/", views.chapters, name="chapters"),
]

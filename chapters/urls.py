from django.urls import path
from . import views

urlpatterns = [
    path("", views.chapters, name="chapters"),
    path('new-chapter/', views.new_chapter, name="new-chapter"),
]

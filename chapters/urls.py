from django.urls import path
from . import views

urlpatterns = [
    path("", views.chapters, name="chapters"),
    path('new-chapter/', views.new_chapter, name="new-chapter"),
    path('join-chapter/', views.join_chapter, name="join-chapter"),
    path('join-us/', views.joinus, name="joinus"),
    path('chapter/<int:chapter_id>/', views.chapterdetails, name="chapterdetails"),
]

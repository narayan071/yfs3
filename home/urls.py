from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("contact/",views.contact,name="contact"),
    path("projects/",views.projects,name="projects"),
    # path("feedback/",views.feedback,name="feedback")
]

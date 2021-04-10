from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("home", views.home_page, name="home_page"),
    path("cv", views.cv_page, name="cv_page"),
    path("volunteering", views.volunteer_page, name="volunteer_page")
]


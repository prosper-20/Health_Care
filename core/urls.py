from django.urls import path
from .views import home

urlapatterns = [
    path("", home, name="home")
]
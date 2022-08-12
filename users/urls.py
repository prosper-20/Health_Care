from django.urls import path
from .views import  signup

urlapatterns = [
    path("signup", signup, name="signup")
]
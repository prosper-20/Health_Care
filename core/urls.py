from django.urls import path
from .views import home, consultation, Home

urlpatterns = [
    path('home/', Home, name="home_1"),
    path("", home, name="home"),
    path("consultation/", consultation, name="consultation")
]
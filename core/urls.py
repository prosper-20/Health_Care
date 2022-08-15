from django.urls import path
from .views import home, consultation, Home, subscription

urlpatterns = [
    path('home/', Home, name="home_1"),
    path("", home, name="home"),
    path("consultation/", consultation, name="consultation"),
    path('subscribe/', subscription, name="subscription")
]
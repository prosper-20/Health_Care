from django.urls import path
from .views import (
    consultation,
    Home, 
    subscription,
    BMIChecker,
    services
)

urlpatterns = [
    path("", Home, name="home"),
    path("consultation/", consultation, name="consultation"),
    path('subscribe/', subscription, name="subscription"),
    path("bmi/checker/", BMIChecker, name="bmi_checker"),
    path("services", services, name="services")
]
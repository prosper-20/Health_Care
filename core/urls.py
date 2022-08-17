from django.urls import path
from .views import (
    consultation,
    Home, 
    subscription,
    BMIChecker,
    services, 
    routine, 
    RoutineCreateView
)

urlpatterns = [
    path("", Home, name="home"),
    path("consultation/", consultation, name="consultation"),
    path('subscribe/', subscription, name="subscription"),
    path("bmi/checker/", BMIChecker, name="bmi_checker"),
    path("services", services, name="services"),
    path("my-routine/", routine, name="routine"),
    path("create/", RoutineCreateView.as_view(), name="create")
   
]
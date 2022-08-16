from django.urls import path
from .views import (
    consultation,
    Home, 
    subscription,
    BMIChecker,
    services, 
    gender,
    motivation,
    focus,
    main_goal
)

urlpatterns = [
    path("", Home, name="home"),
    path("consultation/", consultation, name="consultation"),
    path('subscribe/', subscription, name="subscription"),
    path("bmi/checker/", BMIChecker, name="bmi_checker"),
    path("services", services, name="services"),
    path("gender/", gender, name="gender"),
    path("focus/", focus, name="focus"),
    path("main-goal/", main_goal, name="main_goal"),
    path("motivation/", motivation, name="motivation")
]
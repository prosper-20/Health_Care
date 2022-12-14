from cgi import print_environ
from django.urls import path
from .views import (
    consultation,
    Home, 
    subscription,
    BMIChecker,
    services, 
    routine, 
    RoutineCreateView,
    contact, 
    contact_main,
    about,
    coach, 
    service,
    pricing,
    success_stories,
    service_detail,
    gym

)

urlpatterns = [
    path("", Home, name="home"),
    path("consultation/", consultation, name="consultation"),
    path('subscribe/', subscription, name="subscription"),
    path("bmi/checker/", BMIChecker, name="bmi_checker"),
    path("services", service, name="services"),
    path("my-routine/", routine, name="routine"),
    path("create/", RoutineCreateView.as_view(), name="create"),
    path("contact/", contact_main, name="contact"),
    path("about/", about, name="about"),
    path("coach/", coach, name="coach"),
    path("service", service, name="service"),
    path("service/<slug:slug>/", service_detail, name="service-detail"),
    path("pricing", pricing, name="pricing"),
    path("success-stories/", success_stories, name="success-stories"),
    path("gym/", gym, name="gym")
   
]
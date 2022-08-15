from django.urls import path
from .views import home, consultation

urlpatterns = [
    path("", home, name="home"),
    path("consultation/", consultation, name="consultation")
]
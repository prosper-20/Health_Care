from django.urls import path
from .views import home, detail

urlpatterns = [
    path("", home, name="blog-home"),
    path("<slug:slug>/", detail, name="detail")
]
from django.urls import path
from .views import signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path("signout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout")
]
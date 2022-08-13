from django import forms
from django.contrib.auth.models import User

class UserRegistrationFomr(forms.ModelForm):
    email = forms.EmailField(help_text="Enter a valid email address")
    class Meta:
        model = User

        fields = ["username", 'email', "password", "password2"]
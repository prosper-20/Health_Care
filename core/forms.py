from django import forms
from .models import Consultation, Subscription


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation

        fields = ["first_name", "last_name", "service", "date", "time"]


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription

        fields = ["email"]
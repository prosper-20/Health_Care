from django import forms
from .models import Consultation, Subscription, BMI


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation

        fields = ["first_name", "last_name", "service", "date", "time"]


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription

        fields = ["subscriber_email"]


class BMIForm(forms.ModelForm):
    class Meta:
        model = BMI

        fields = ["weight", "height"]

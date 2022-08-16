from django import forms
from .models import Consultation, Subscription, BMI, Question


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


class GenderForm(forms.ModelForm):
    class Meta:
        model = Question

        fields = ["gender"]

class FocusForm(forms.ModelForm):
    class Meta:
        model = Question

        fields = ["focus"]

class MainGoalForm(forms.ModelForm):
    class Meta:
        model = Question

        fields = ["main_goal"]

class MotivationForm(forms.ModelForm):
    class Meta:
        model = Question

        fields = ["motivation"]


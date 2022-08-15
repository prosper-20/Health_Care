from django import forms
from .models import Consultation


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation

        fields = ["first_name", "last_name", "service", "date", "time"]
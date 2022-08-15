from django.shortcuts import render
from .forms import ConsultationForm
from .models import Consultation
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def consultation(request):
    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, )



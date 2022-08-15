from django.shortcuts import render, redirect
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
            username = form.cleaned_data.get("first")
            messages.success(request, f"Hi {username}, you have successfully booked a session with us.. see you soon")
            return redirect('home')

    else:
        form = ConsultationForm()

    context = {
        "form": form
    }
    return render(request, "core/consultation.html", context)
        



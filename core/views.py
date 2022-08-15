from this import d
from django.shortcuts import render, redirect
from .forms import ConsultationForm
from .models import Consultation
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get('last_name')
        service = request.POST.get("service")
        date = request.POST.get("date")
        time = request.POST.get("time")

        consultation = Consultation.objects.create(
            first_name = first_name,
            last_name = last_name,
            service = service,
            date = date,
            time = time
        )
        consultation.save()
        messages.success(request, f"Hi {first_name}, you have successfully booked a session with us.. see you soon")
        return redirect("home")
    
    else:
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



# def consultation_main(request):
#     if request.method == "POST":
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get('last_name')
#         service = request.POST.get("service")
#         date = request.POST.get("date")
#         time = request.POST.get("time")

#         consultation = Consultation.objects.create(
#             first_name = first_name,
#             last_name = last_name,
#             service = service,
#             date = date,
#             time = time
#         )
#         consultation.save()
#         messages.success(request, f"Hi {first_name}, you have successfully booked a session with us.. see you soon")
#         return redirect("home")
    
#     else:
#         return render(request, "")
        



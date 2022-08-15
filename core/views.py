import email
from this import d
from django.shortcuts import render, redirect
from .forms import ConsultationForm, SubscriptionForm, BMIForm
from .models import Consultation, Subscription, BMI
from django.contrib import messages

# Create your views here.

# def home(request):
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
#         return render(request, 'core/home.html')


def Home(request):
    if request.method == "POST":
        if "first_name" in request.POST:
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
        elif "subscriber_email" in request.POST:
            subscriber_email = request.POST.get("subscriber_email")
            subscriber = Subscription.objects.create(subscriber_email=subscriber_email)
            subscriber.save()
            messages.success(request, 'You have successfully subscribed to our newsletter!')
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


def subscription(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for subscribing')
            return redirect('home')
    else:
        form = SubscriptionForm()
    context = {
        "form": form
    }
    
    return render(request, 'core/subscription.html', context)
        

def BMIChecker(request):
    if request.method == "POST":
        form = BMIForm(request.POST)
        if form.is_valid():
            form.save()
            weight = form.cleaned_data.get("weight")
            height = form.cleaned_data.get("height")

            BMI_Index = weight // (height ** 2)

            if BMI_Index > 25:
                messages.warning(request, f"Your BMI index is {BMI_Index}, you are overweight!")
                return redirect("home")
            elif BMI_Index < 25:
                messages.success(request, f"Your BMI index is {BMI_Index}, you are healthy!")
                return redirect("home")
            else:
                messages.error(request, "Invalid values entered..please try again")
                return redirect("home")

    else:
        form = BMIForm()

    context = {
        "form": form
    }
    
    return render(request, 'core/bmi_checker.html', context)





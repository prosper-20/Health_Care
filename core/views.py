import email
from sys import flags
from this import d
from django.shortcuts import render, redirect
from .forms import ConsultationForm, SubscriptionForm, BMIForm, GenderForm, FocusForm, MainGoalForm, MotivationForm
from .models import Consultation, Subscription, BMI, Question
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
           

            metre_height = height / 100

            BMI_Index = int(weight // (metre_height ** 2))
            print(BMI_Index)
            print(type(BMI_Index))

           

            if BMI_Index in range (25, 30):
                messages.warning(request, f"Your BMI index is {BMI_Index}, you are overweight!")
                return redirect("home")
            elif BMI_Index in range(18, 25):
                messages.success(request, f"Your BMI index is {BMI_Index}, you are healthy!")
                return redirect("home")
            elif BMI_Index > 30:
                messages.warning(request, f"Your BMI index is {BMI_Index}, you are obese!")
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

def services(request):
    return render(request, 'core/services.html')


def gender(request):
    if request.method == "POST":
        form = GenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("focus")
    else:
        form = GenderForm()
    context = {
        "form": form
    }
    return render(request, "core/gender.html", context)


def focus(request):
    if request.method == "POST":
        form = FocusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_goal")
    else:
        form = FocusForm()
    context = {
        "form": form
    }
    return render(request, "core/focus.html", context)


def main_goal(request):
    if request.method == "POST":
        form = MainGoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("motivation")
    else:
        form = MainGoalForm()
    context = {
        "form": form
    }
    return render(request, "core/main_goal.html", context)


def motivation(request):
    if request.method == "POST":
        form = MotivationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MotivationForm()
    context = {
        "form": form
    }
    return render(request, "core/motivation.html", context)






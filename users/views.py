from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hi {username}, your account has been created successfully!")
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        "form": form
    }
    return render(request, 'users/signup.html', context)



def signup_main(request):
    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get("password2")
        

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username '{username}' already exists")
            return redirect("signup")
        
        elif User.objects.filter(email=email).exists:
            messages.error("Sorry, the email already belongs to another user.")
            return redirect('signup')
        
        elif password != password2:
            messages.error("Both passwords must match!")
            return redirect("signup")
        else:
            user = User.objects.create(
                username = username,
                email = email,
                password = password
            )
            user.save()
            messages.success(request, f"Hi, {username}, your account has been created successfully!")
            return redirect("signin")
    else:
        return render(request, "users/register.html")




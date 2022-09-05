# How to integrate Twilio Sendgrid into your Django Application
 
Hey guys, 

Today, we will be learning how to integrate Twilio Sendgrid into our Django Application. For those who do not know what Twilio Sendgird is, here's a brief introduction. Sendgrid is a customer communication platform for transactional and marketing email. If that definition doesn't ring a bell, do not be alarmed, the use case will shed some light.

## Use Case
Have you ever wondered how welcome emails are sent whenever you sign up on a platform? How is the process automated? How does the platform know the user to send the mail to? How does the platform send you marketing emails informing you of new products/policies or services. The answer to these questions is SendGrid. For those who aren't aware of what Twilio Sendgird is, here's a brief introduction.
SendGrid is a cloud-based SMTP provider that allows you to send emails without having to maintain email servers. SendGrid manages all of the technical details, from scaling the infrastructure to ISP outreach and reputation monitoring to whitelist services and real-time analytics.

## Benefits of using Sendgrid
The main benefits of SendGrid are its:
 
1. Deliverability: Most email issues are a result of poor deliverability. SendGrid offers excellent deliverability packages that review, analyzes, and diagnose email program and make recommendations.

2. Scalability: Sendgrid can be integrated into businesses ranging from small enterprises/startups to high-volume senders or marketers. With SendGrid, there's a plan for everyone.

3. Reliability: In 2021, SendGrid processed a staggering 7 billion emails on Cyber Monday and 6.8 billion emails on Black Friday. But more importantly, the SendGrid platform performed brilliantly during this peak sending holiday, ensuring that our customers’ emails reached inboxes.

### Table of Content
1. Introduction 
2. Use Cases
3. Benefits of using SendGrid
4. Creating a Python Environment
5. Creating a Django Application
6. Creating HTML Templates
7. Setting Up User Registration
8. Setting up the URLs
9. Integrating Sendgrid
10. Additional Resources


For simplicity, I'm going to be building a User Registration Web Application using Django. The objective of this project is to send a welcome email whenever a user signs up on our web application.


## Step 1: Create your Python Environment
Open your command prompt/termainal and input the following:

> `cd` desktop. # Change directory into your desktop
> 
> `mkdir Sendgrid` # Create a directory called Sendgrid
> 
> `cd Sendgrid`. # hange directory into Sendgrid
> 
> `virtualenv <env>` # Create a virtual environment named 'env'   
>
> `.\env\scripts\activate`Activate the virtual environment for Windows Users
> 
> `source ./env/scripts/bin/activate`Activate the virtual environment for  Mac/Linux Users

## Step 2: Create A Django Application
Run the following command;
> `pip install django`

Next, run `django-admin startproject PROJECT` in your terminal. Now, `cd` into the project via this command `cd PROJECT`.

Lastly, we're going to create our `users` application. To do this, run the following command:
> `python manage.py startapp users`

We need to register our `users` application in the main project folder. Head on to your `PROJECT/settings.py`. Add the following code to your `INSTALLED_APPS`

![alt text](https://prosper-django-bucket.s3.us-east-2.amazonaws.com/Screenshot+(46).jpg)

To verify if our setup was successful, run `python manage.py runserver`.
![alt text](https://prosper-django-bucket.s3.us-east-2.amazonaws.com/Screenshot+(48).jpg)  If you got an output similar to the image above, 
congratulations on making it this far.

Next, run the following commands: 
> `python manage.py migrate` 
> 
> `python manage.py createsuperuser` 



## Step 3: Creating HTML Templates and Static Files
This project requires just three HTML files: `home.html`, `register.html`, and `base.html`. Open your IDE, and create a folder named `templates` in the app directory. Next, create another folder named `users` inside the newly created `templates` folder. Doing this enables django to locate the `HTML` Templates.
Your folder structure should be like this:

(![alt text](https://prosper-django-bucket.s3.us-east-2.amazonaws.com/Screenshot+(54).jpg) 





Copy and paste the following code accordingly:

`base.html`

    {% load static %}
    <!DOCTYPE html>
    <html>
    <head>
    
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    
        <link rel="stylesheet" type="text/css" href="{% static 'users/main.css' %}">
    
        {% if title %}
            <title>My App - {{ title }}</title>
        {% else %}
            <title>My App</title>
        {% endif %}
        </head>
        <body>
        <header class="site-header">
          <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
            <div class="container">
              <a class="navbar-brand mr-4" href="{% url 'home' %}">MY APP</a>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarToggle">
                <div class="navbar-nav mr-auto">
                  <a class="nav-item nav-link" href="{% url 'home' %}">Home</a>
                  <a class="nav-item nav-link" href="">About</a>
                </div>
                <!-- Navbar Right Side -->
                <div class="navbar-nav">
                    <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
                </div>
              </div>
            </div>
          </nav>
        </header>
        <main role="main" class="container">
          <div class="row">
            <div class="col-md-8">
              {% if messages %}
                {% for message in messages %}
                  <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                  </div>
                {% endfor %}
              {% endif %}
              {% block content %}{% endblock %}
            </div>
            <div class="col-md-4">
              <div class="content-section">
                <h3>Our Sidebar</h3>
                <p class='text-muted'>You can put any information here you'd like.
                  <ul class="list-group">
                    <li class="list-group-item list-group-item-light">Latest Posts</li>
                    <li class="list-group-item list-group-item-light">Announcements</li>
                    <li class="list-group-item list-group-item-light">Calendars</li>
                    <li class="list-group-item list-group-item-light">etc</li>
                  </ul>
                </p>
              </div>
            </div>
          </div>
        </main>
    
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        </body>
        </html>     

`register.html`

    {% extends "users/base.html" %}
    {% load crispy_forms_tags %}
    {% block content %}
        <div class="content-section">
            <form method="POST">
                {% csrf_token %}
                <fieldset class="form-group">
                    <legend class="border-bottom mb-4">Join Today</legend>
                    {{ form|crispy }}
                </fieldset>
                <div class="form-group">
                    <button class="btn btn-outline-info" type="submit">Sign Up</button>
                </div>
            </form>
            <div class="border-top pt-3">
                <small class="text-muted">
                    Already Have An Account? <a class="ml-2" href="">Sign In</a>
                </small>
            </div>
        </div>
    {% endblock content %}


`home.html`

    {% extends "users/base.html" %}
    {% block content %}
        <h1>Home Page</h1>
    {% endblock content %}

`index.html`
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Welcome Email</title>
      </head>
      <body>
          Welcome to my Web Application
      </body>
      </html>

  Run `pip install django-crispy-forms` and add to the `INSTALLED_APPS` `crispy_forms`. Your `INSTALLED_APP` should look like this now.
![alt text](https://prosper-django-bucket.s3.us-east-2.amazonaws.com/Screenshot+(50).png) 

  Navigate to the last line of the project's `settings.py` and input this line of code:
  > `CRISPY_TEMPLATE_PACK = "bootstrap4"`

  ![alt text](https://prosper-django-bucket.s3.us-east-2.amazonaws.com/Screenshot+(61).jpg)

## Setting up the static files
Similar to the way we created our HTML files, create a folder named `static` in the `users` app. Create another folder called `users` inside the just created `static` folder. Lastly, create a file named `main.css` and paste the following code.

Your setup should be similar to this

![alt text](https://prosper-django-bucket.s3.us-east-2.amazonaws.com/Screenshot+(56).jpg) 

Copy and paste the following code into the `main.css` file

  `main.css`

    body {
      background: #fafafa;
      color: #333333;
      margin-top: 5rem;
    }
    
    h1, h2, h3, h4, h5, h6 {
      color: #444444;
    }
    
    ul {
      margin: 0;
    }
    
    .bg-steel {
      background-color: #5f788a;
    }
    
    .site-header .navbar-nav .nav-link {
      color: #cbd5db;
    }
    
    .site-header .navbar-nav .nav-link:hover {
      color: #ffffff;
    }
    
    .site-header .navbar-nav .nav-link.active {
      font-weight: 500;
    }
    
    .content-section {
      background: #ffffff;
      padding: 10px 20px;
      border: 1px solid #dddddd;
      border-radius: 3px;
      margin-bottom: 20px;
    }
    
    .article-title {
      color: #444444;
    }
    
    a.article-title:hover {
      color: #428bca;
      text-decoration: none;
    }
    
    .article-content {
      white-space: pre-line;
    }
    
    .article-img {
      height: 65px;
      width: 65px;
      margin-right: 16px;
    }
    
    .article-metadata {
      padding-bottom: 1px;
      margin-bottom: 4px;
      border-bottom: 1px solid #e3e3e3
    }
    
    .article-metadata a:hover {
      color: #333;
      text-decoration: none;
    }
    
    .article-svg {
      width: 25px;
      height: 25px;
      vertical-align: middle;
    }
    
    .account-img {
      height: 125px;
      width: 125px;
      margin-right: 20px;
      margin-bottom: 16px;
    }
    
    .account-heading {
      font-size: 2.5rem;
    }

Create a `forms.py` in the `users` app and paste the following code:

        from django import forms
        from django.contrib.auth.models import User
        from django.contrib.auth.forms import UserCreationForm
        
        class UserRegistrationForm(UserCreationForm):
            email = forms.EmailField(help_text="Enter a valid email address")
            class Meta:
                model = User
        
                fields = ["username", 'email', "password1", "password2"]

## Step 4: Creating User Registration View
Go into your `users/view.py` file and input the following code:

`views.py`

    from django.shortcuts import render

    # Create your views here.
    from django.shortcuts import render, redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.models import User
    from .forms import UserRegistrationForm
    from django.contrib import messages
    
    from django.conf import settings
    from django.core.mail import EmailMessage, send_mail
    from django.template.loader import render_to_string
    from django.core.mail import EmailMessage, send_mail
    from sendgrid.helpers.mail import SandBoxMode, MailSettings


    def register(request):
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                email = form.cleaned_data.get("email")
                mydict = {'username': username}
                html_template = 'users/index.html'
                html_message = render_to_string(html_template, context=mydict)
                subject = 'Welcome to My App'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                message = EmailMessage(subject, html_message,
                email_from, 
                recipient_list)
                message.content_subtype = 'html'
                message.send()
                messages.success(request, f"Hi {username}, your account has been created successfully!")
                return redirect("home")
        else:
            form = UserRegistrationForm()
    
        context = {
            "form":form
        }
        return render(request, 'users/register.html', context)
    
    def home(request):
        return render(request, "users/home.html")

The `index.html` file is the Html template that's automatically sent to the user upon registration.

## Step : Setting up the PROJECT'S URLS.py
In the main project's urls file, add the following code:
![alt text](https://prosper-django-bucket.s3.us-east-2.amazonaws.com/Screenshot+(59).png) 

In the `users` app, create a `urls.py` file and insert the following code:

    from django.urls import path
    from .views import register, home
    
    urlpatterns = [
        path("", home, name="register"),
        path("register/", register, name="home"),
        
    ]



## Step 5: Setting up Sendgrid In your Project
To make use of SendGrid, it is necessary to install it in our virtual environment. Run the code below in your terminal.

>`pip install sendgrid-django` 

Copy and paste the following code in your Project's `settings.py` file



## Step 6: Testing our code
At this point, it is safe to say we have configured our application accordingly. Now, we have to register a new user with a valid email address.
Run `python manage.py runserver` in your terminal. Open your browser and click on the register link on the right hand side of the navbar.

** NOTE: Ensure the email entered is a valid one, so as to receive the signup welcome email**

## Step 7: Conclusion
Now that we have a basic idea of Twilio SendGrid, feel free to explore some of its other amazing features.

** Thank you for reading! **












  


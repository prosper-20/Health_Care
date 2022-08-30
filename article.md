# How to integrate Twilio Sendgrid into Django Application

Hey guys, 

Today, i'm going to be teaching you how to integrate Twilio Sendgrid in your Django Application using minimal effort. For those who aren't aware what Twilio Sendgirdis, here's a brief Introduction. Sendgrid is simply a customer communication platform for transactional and marketing email. If that definition didn't ring a bell, do not be alarmed, the use case will shed some light.

### Table of Content
- Introduction 
- Use Cases
- Benefits if using sendgrid
- Creating a Python Environment
- Creating a Django Application
- Creating HTML Templates
- Setting Up User Registration
- Testing
- Conclusion 
- Additional Resources

## Use Case
Have you ever wondered how welcome mails are sent whenver you sign up on a platform? How is the process automated? How does the platform know the user to send the mail to? This is where Sendgrid comes in.
SendGrid is based on acloud-based SMTP provider that allows you to send emails without having to maintain email servers. SendGrid manages all of the technical details, from scaling the infrastructure to ISP outreach and reputation monitoring to whitelist services and real time analytics.

## Benefits of using Sendgrid
The main benefits of SendGrid are its deliverability, its scalability, and its reliability. Read on to know more of its benefits.


For simplicity, i'm going to be building a User Registration Web Application using Django.


## Step 1: Create your Python Environment
To create a virtual environment, simply run
> `virtualenv <env>`    NOTE: You can name your virtual environment anything you want.

Next, activate the virtual environment by running the following command:

> `.\env\scripts\activate` For Windows Users
> 
> `source ./env/scripts/bin/activate` For Mac/Linux Users

## Step 2: Set Up your Django Application
Run the followinng command;
> `pip install django`

Next, run `djang-admin startproject PROJECT` in your terminal

Next
> `cd PROJECT`
>
Lasttly, we're going to create our `users` application. To do this, run the following command:
> `python manage.py startapp users`

We need to register our `users` application in the main project folder. To do this, simply head on to the your `PROJECT/settings.py`. 

To verify if our setup was successful, run `python manage.py runserver`. If you get an output similar to this, Congratulations on making this far.


## Step 3: Creating HTML Templates
This project requires just three HTML files: `home.html`, `register.html`, `base.html`. Open your IDE, create a folder named `templates` in the app directory. Next, create another folder named after the application, in our case `users`. The following set up is to enable our project locate the `HTML` Templates.

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

    <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

    {% if title %}
        <title>Django Blog - {{ title }}</title>
    {% else %}
        <title>Django Blog</title>
    {% endif %}
    </head>
    <body>
    <header class="site-header">
      <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
        <div class="container">
          <a class="navbar-brand mr-4" href="{% url 'blog-home' %}">Django Blog</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarToggle">
            <div class="navbar-nav mr-auto">
              <a class="nav-item nav-link" href="{% url 'blog-home' %}">Home</a>
              <a class="nav-item nav-link" href="{% url 'blog-about' %}">About</a>
            </div>
            <!-- Navbar Right Side -->
            <div class="navbar-nav">
              {% if user.is_authenticated %}
                <a class="nav-item nav-link" href="{% url 'post-create' %}">New Post</a>
                <a class="nav-item nav-link" href="{% url 'profile' %}">Profile</a>
                <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
              {% else %}
                <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
                <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
              {% endif %}
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

    {% extends "blog/base.html" %}
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
                    Already Have An Account? <a class="ml-2" href="{% url 'login' %}">Sign In</a>
                </small>
            </div>
        </div>
    {% endblock content %}


`home.html`

    {% extends "blog/base.html" %}
    {% block content %}
        <h1>Home Page</h1>
    {% endblock content %}



## Step 4: Creating User Registration View
Go into your `users/view.py` file and input the folloeing code:














  


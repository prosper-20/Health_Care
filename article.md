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












  


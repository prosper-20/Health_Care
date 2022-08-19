from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

SERVICES_CHOICES = (
    (
        ("Gym Session", "Gym Session"),
        ("Therapy Session", "Therapy Session"),
        ("Massage", "Massage"),
        ("Spa", "Spa"),
        ("Healthy Food", "Healthy Food")
    )
)

GOAL_CHOICES = (
    ("Lose weight", "Lose weight"),
    ("Build Muscles", "Build Muscles"),
    ("Keep Fit", "Keep Fit")
)


TIME_CHOICES = (
    ("8:00AM", "8:00AM"),
    ("9:00AM", "9:00 AM"),
    ("10:00AM", "10:00 AM"),
    ("11:00AM", "11:00 AM"),
    ("12:00PM", "12:00 PM"),
    ("1:00PM", "1:00 PM"),
    ("2:00PM", "2:00 PM"),
    ("3:00PM", "3:00 PM"),
    ("4:00PM", "4:00 PM"),
    ("5:00PM", "5:00 PM"),
    ("6:00PM", "6:00 PM"),
    ("7:00PM", '7:00 PM')
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female")
)

BODY_CHOICES = (
    ("Chest", "Chest"),
    ("Abs", "Abs"),
    ("Arms", "Arms"),
    ("Legs", "Legs")
)

MOTIVATION_CHOICES = (
    ("Feel Confident", "Feel Confident"),
    ("Release Stress", "Release Stress"),
    ("Improve Health", "Improve Health"),
    ("Boost Energy", "Boost Energy")
)

ACTIVITY_LEVEL_CHOICES = (
    ("Sedentary", "Sedentary"),
    ("Lightly Active", "Lightly Active"),
    ("Moderately Active", "Moderately Active"),
    ("Very Active", "Very Active")
)



class Consultation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    service = models.CharField(choices=SERVICES_CHOICES, max_length=100)
    date = models.CharField(help_text="Choose a date", max_length=50)
    time = models.CharField(choices=TIME_CHOICES, max_length=50)

    def __str__(self):
        return self.first_name


class Subscription(models.Model):
    subscriber_email = models.EmailField()

    def __str__(self):
        return self.subscriber_email


class BMI(models.Model):
    weight = models.FloatField(help_text="Kg")
    height = models.FloatField(help_text="Cm")

    def bmi_result(self):
        return self.weight // (self.height ** 2)


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    focus = models.CharField(choices=BODY_CHOICES, max_length=50)
    main_goal = models.CharField(choices=GOAL_CHOICES, max_length=50)
    motivation = models.CharField(choices=MOTIVATION_CHOICES, max_length=100)

    def __str__(self):
        return self.user


class Personalization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    focus = models.CharField(choices=BODY_CHOICES, max_length=50)
    main_goal = models.CharField(choices=GOAL_CHOICES, max_length=50)
    motivation = models.CharField(choices=MOTIVATION_CHOICES, max_length=100)
    activity_level = models.CharField(choices=ACTIVITY_LEVEL_CHOICES, max_length=100)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("home")


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="coach_pictures")
    job_title = models.CharField(max_length=100)
    about = models.TextField()

    class Meta:
        verbose_name_plural = "coaches"

    def __str__(self):
        return self.name




from django.contrib import admin
from .models import (
        Consultation,
        Subscription, 
        Question, 
        Personalization,
        Contact,
        Coach
)

# Register your models here.

class ConsultationAdmin(admin.ModelAdmin):
        list_display = ["first_name", "last_name", "service", "date", "time"]



admin.site.register(Consultation, ConsultationAdmin)


admin.site.register(Subscription)


class QuestionAdmin(admin.ModelAdmin):
        list_display = ["user", "gender", "focus", "main_goal", "motivation"]


admin.site.register(Question, QuestionAdmin)


class PersonalizationAdmin(admin.ModelAdmin):
        list_display = ["user", "gender", "focus", "main_goal", "motivation", "activity_level"]


admin.site.register(Personalization, QuestionAdmin)


class ContactAdmin(admin.ModelAdmin):
        list_display = ["name", "email", "subject"]


admin.site.register(Contact, ContactAdmin)

class CoachAdmin(admin.ModelAdmin):
        list_display = ["name", "job_title", "about"]


admin

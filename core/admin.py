from django.contrib import admin
from .models import Consultation, Subscription, Question

# Register your models here.

class ConsultationAdmin(admin.ModelAdmin):
        list_display = ["first_name", "last_name", "service", "date", "time"]



admin.site.register(Consultation, ConsultationAdmin)


admin.site.register(Subscription)


class QuestionAdmin(admin.ModelAdmin):
        list_display = ["question", "gender", "focus"]

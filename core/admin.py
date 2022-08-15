from django.contrib import admin
from .models import Consultation, Subscription

# Register your models here.

class ConsultationAdmin(admin.ModelAdmin):
        list_display = ["first_name", "last_name", "service", "date", "time"]



admin.site.register(Consultation, ConsultationAdmin)


admin.site.register(Subscription)

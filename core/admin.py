from django.contrib import admin
from .models import Consultation

# Register your models here.

class ConsultationAdmin(admin.ModelAdmin):
        list_display = ["first_name", "last_name", "service", "date", "time"]



admin.site.register(Consultation, ConsultationAdmin)

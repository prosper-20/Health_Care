from django.contrib import admin
from .models import Consultation

# Register your models here.

class ConsultationAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ["first", "last", "service", "date"]



admin.site.register(Consultation, ConsultationAdmin)

from django.contrib import admin
from .models import Post, Tags

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", 'author', "date_posted"]



admin.site.register(Post, PostAdmin)

admin.site.register(Tags)

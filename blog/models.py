from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default="post.jpg", upload_to="post_pictures")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("deatil", args=[str(self.slug)])
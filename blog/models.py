from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# TAG_CHOICES = (
#     ("Food", "Food"),
#     ("Life", "Life"),
#     ("Coach", "Coach"),
#     ("Healthy", "Healthy"),
#     ("Lifestyle", "Lifestyle"),
#     ("Green", "Green"),
#     ("Exercise", "Exercise"),
#     ("Dietician", "Dietician")
# )

class Tags(models.Model):
    choice = models.CharField(max_length=154)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.choice



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default="post.jpg", upload_to="post_pictures")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    tags = models.ManyToManyField(Tags, related_name='tags')
    

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("detail", args=[str(self.slug)])
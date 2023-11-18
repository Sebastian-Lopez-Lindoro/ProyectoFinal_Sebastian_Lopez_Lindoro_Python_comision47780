from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(
        max_length=150,
    )
    subtitle = models.CharField(max_length=150, null=True)
    body = models.CharField(max_length=150, null=True)
    author = models.CharField(max_length=150, null=True)
    date = models.DateField(
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)

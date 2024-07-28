
from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)  # Add this if you want to manage an image

    def __str__(self):
        return self.title

class Fact(models.Model):
    icon_class = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.title
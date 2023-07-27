from django.db import models

# Create your models here.

class Settings(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='settings/')
    description = models.TextField(max_length=1500)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    fb_link = models.URLField(max_length=500)
    x_link = models.URLField(max_length=500)
    insta_link = models.URLField(max_length=500)

    def __str__(self):
        return self.name
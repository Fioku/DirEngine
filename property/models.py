from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='property/')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=2000)
    place = models.ForeignKey('Place', related_name='property_place', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='property_category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    

class Images(models.Model):
    property = models.ForeignKey(Property, related_name='image', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='property/images/')
    
    def __str__(self):
        return str(self.property)

class Place(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='places/')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Property_Rate(models.Model):
    auther = models.ForeignKey(User, related_name='auther_rate', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='property_review', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return self.name
    
count = {
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
}

class PropertyBook(models.Model):
    auther = models.ForeignKey(User, related_name='auther_booking', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='property_booking', on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    guest = models.CharField(max_length=2, choices=count)
    children = models.CharField(max_length=2, choices=count)
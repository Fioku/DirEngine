from django.contrib import admin
from .models import Property, Images, Place, Category, Property_Rate, PropertyBook

# Register your models here.

admin.site.register(Property)
admin.site.register(Images)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(Property_Rate)
admin.site.register(PropertyBook)
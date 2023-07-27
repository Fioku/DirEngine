from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Property

class PropertyListView(ListView):
    model = Property
    

class PropertyDetails(DetailView):
    pass
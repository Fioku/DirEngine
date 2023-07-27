from django.urls import path
from .views import PropertyListView, PropertyDetails
app_name = 'property'

urlpatterns = [
    path('', PropertyListView.as_view()),
    # path('',),
]
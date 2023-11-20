from django.urls import path
from .views import initialize_elevator_system

urlpatterns = [
   path('initialize_elevator_system/', initialize_elevator_system, name='initialize_elevator_system'),
]
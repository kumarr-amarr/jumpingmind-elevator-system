from django.urls import path
from .views import initialize_elevator_system, open_door, close_door

urlpatterns = [
   path('initialize_elevator_system/', initialize_elevator_system, name='initialize_elevator_system'),
   path('open_door/', open_door, name='open_door'),
   path('close_door/', close_door, name='close_door'),
]
from django.urls import path
from .views import initialize_elevator_system, open_door, close_door, move_elevator_up, move_elevator_down

urlpatterns = [
   path('initialize_elevator_system/', initialize_elevator_system, name='initialize_elevator_system'),
   path('open_door/', open_door, name='open_door'),
   path('close_door/', close_door, name='close_door'),
   path('move_elevator_up/', move_elevator_up, name='move_elevator_up'),
   path('move_elevator_down/', move_elevator_down, name='move_elevator_down'),
]
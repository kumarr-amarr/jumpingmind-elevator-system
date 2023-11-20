from django.urls import path
from .views import (
   initialize_elevator_system,
   open_door,
   close_door,
   move_elevator_up,
   move_elevator_down,
   fetch_next_destination,
   stop_elevator,
   save_user_request,
   fetch_requests_for_elevator,
   update_elevator_status,
   mark_elevator_operational,
   mark_elevator_non_operational,
   fetch_elevator_direction,
)

urlpatterns = [
   path('initialize_elevator_system/', initialize_elevator_system, name='initialize_elevator_system'),
   path('open_door/', open_door, name='open_door'),
   path('close_door/', close_door, name='close_door'),
   path('move_elevator_up/', move_elevator_up, name='move_elevator_up'),
   path('move_elevator_down/', move_elevator_down, name='move_elevator_down'),
   path('fetch_next_destination/', fetch_next_destination, name='fetch_next_destination'),
   path('fetch_elevator_direction/', fetch_elevator_direction, name='fetch_elevator_direction'),
   path('stop_elevator/', stop_elevator, name='stop_elevator'),
   path('save_user_request/', save_user_request, name='save_user_request'),
   path('fetch_requests_for_elevator/', fetch_requests_for_elevator, name='fetch_requests_for_elevator'),
   path('update_elevator_status/', update_elevator_status, name='update_elevator_status'),
   path('mark_elevator_operational/', mark_elevator_operational, name='mark_elevator_operational'),
   path('mark_elevator_non_operational/', mark_elevator_non_operational, name='mark_elevator_non_operational'),
]
from django.urls import path
#imported views functions in a tupple
from .views import (
   initialize_elevator_system,
   fetch_requests_for_elevator,
   fetch_next_destination,
   save_user_request,
   update_elevator_status,
   open_door,
   close_door,
   move_elevator_up,
   move_elevator_down,
   stop_elevator,
   mark_elevator_operational,
   mark_elevator_non_operational,
   fetch_elevator_direction,
)

#defines urls path for http request, shows how apis will be called 
urlpatterns = [
   path('initialize_elevator_system/', initialize_elevator_system, name='initialize_elevator_system'),
   path('fetch_requests_for_elevator/', fetch_requests_for_elevator, name='fetch_requests_for_elevator'),
   path('fetch_next_destination/', fetch_next_destination, name='fetch_next_destination'),
   path('fetch_elevator_direction/', fetch_elevator_direction, name='fetch_elevator_direction'),  
   path('save_user_request/', save_user_request, name='save_user_request'),
   path('update_elevator_status/', update_elevator_status, name='update_elevator_status'),
   path('open_door/', open_door, name='open_door'),
   path('close_door/', close_door, name='close_door'),
   path('move_elevator_up/', move_elevator_up, name='move_elevator_up'),
   path('move_elevator_down/', move_elevator_down, name='move_elevator_down'),
   path('stop_elevator/', stop_elevator, name='stop_elevator'),
   path('mark_elevator_operational/', mark_elevator_operational, name='mark_elevator_operational'),
   path('mark_elevator_non_operational/', mark_elevator_non_operational, name='mark_elevator_non_operational'),
]
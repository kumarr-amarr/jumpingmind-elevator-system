from django.contrib import admin
from .models import Floor,Elevator,UserRequest

# I have register my models here.
@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    #customize how the models are displayed
    list_display = ('floor_number', )

@admin.register(Elevator)
class ElevetorAdmin(admin.ModelAdmin):
    list_display = ('elevator_id', 'current_floor', 'direction', 'door_status', 'running', 'operational')
    #add filters and search capabilities to the admin interface
    list_filter = ('direction', 'door_status', 'running', 'operational')

@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('elevator', 'floor_number', 'direction')
    list_filter = ('direction', )
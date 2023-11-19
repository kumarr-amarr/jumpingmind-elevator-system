from django.contrib import admin
from .models import Floor,Elevator,UserRequest

# Register your models here.
@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('floor_number', )

@admin.register(Elevator)
class ElevetorAdmin(admin.ModelAdmin):
    list_display = ('elevator_id', 'current_floor', 'direction', 'door_status', 'running', 'operational')
    list_filter = ('direction', 'door_status', 'running', 'operational')

@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('elevator', 'floor_number', 'direction')
    list_filter = ('direction', )
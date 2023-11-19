from django.contrib import admin
from .models import Floor,Elevator,UserRequest

# Register your models here.
@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    pass

@admin.register(Elevator)
class ElevetorAdmin(admin.ModelAdmin):
    pass

@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    pass
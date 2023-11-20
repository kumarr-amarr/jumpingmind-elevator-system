from django.db import models

#This class is Floor that defines number of floor in a building.
class Floor(models.Model):
    floor_number = models.IntegerField()

#This is Elevator and it defines the properties of Elevators .
class Elevator(models.Model):
    elevator_id = models.IntegerField(primary_key=True)
    current_floor = models.IntegerField()
    direction = models.CharField(max_length=4, default="stop")
    door_status = models.CharField(max_length=6, default="closed")
    running = models.BooleanField(default=False)
    operational = models.BooleanField(default=True)

#This is class that defines user request for lift they are going to use  
class UserRequest(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor_number = models.IntegerField()
    direction = models.CharField(max_length=4)
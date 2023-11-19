from django.db import models

class Floor(models.Model):
    floor_number = models.integerField()

class Elevator(models.Model):
    elevator_id = models.integerField(primary_key=True)
    current_floor = models.integerField()
    direction = models.charField(max_length=4, default="stop")
    door_status = models.CharField(max_length=6, default="closed")
    running = models.BooleanField(default=False)
    operational = models.BooleanField(default=True)

class UserRequest(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor_number = models.IntegerField()
    direction = models.CharField(max_length=4)



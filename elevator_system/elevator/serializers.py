from rest_framework import serializers
from.models import Floor, Elevator, UserRequest

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = '__all__'
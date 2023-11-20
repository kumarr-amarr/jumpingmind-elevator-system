from rest_framework import serializers
from.models import Floor, Elevator, UserRequest

# These are serializers classes serialize mosels using this convert complex datatypes into jJSON format.
#So, I have serialize all models for parsing data in simplest form.

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        #defines model for database table
        model = Floor
        # Here I have defines alll properties of model class in a shortcut form that point database fields
        fields = '__all__'

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = '__all__'
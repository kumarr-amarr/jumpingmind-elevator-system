from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from.models import Elevator, UserRequest
from .serializers import UserRequestSerializer

#This function initialize elevator system
@api_view(['POST'])
def initialize_elevator_system(request):
    # try to retrieve the number of elevators from the request data
    try:
        num_elevators = int(request.data.get('num_elevators', 0))
    except ValueError:
        # Returns 400 Bad Request response if the given value is not a valid integer
        return Response({'error': 'Invalid number of elevators. Must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Check if the number of elevators is not a positive integer
    if num_elevators <= 0:
        # Returns 400 Bad Request response for an invalid number of elevators
        return Response({'error': 'Invalid number of elevators'}, status=status.HTTP_400_BAD_REQUEST)

    for i in range(1, num_elevators + 1):
        # Initialize specified number of elevators with initial floor of 1
        Elevator.objects.create(elevator_id=i, current_floor=1)

    # Returns 201 Created response on successful initialization
    return Response({'message': f'{num_elevators} elevators initialized successfully'}, status=status.HTTP_201_CREATED)

#this function fetch requested data for user request
@api_view(['GET'])
def fetch_requests_for_elevator(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    requests = UserRequest.objects.filter(elevator=elevator)
    serializer = UserRequestSerializer(requests, many=True)
    return Response(serializer.data)

#this fetch what should be the next destination of elevator
@api_view(['GET'])
def fetch_next_destination(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    next_destination = elevator.userrequest_set.first()
    
    if next_destination is not None:
        return Response({'next_destination': next_destination.floor_number})
    else:
        return Response({'message': 'No pending requests'}, status=status.HTTP_204_NO_CONTENT)
    
#this fetch what is  direction of elevator
@api_view(['GET'])
def fetch_elevator_direction(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    return Response({'direction': elevator.direction})

#this function take user request, which floor thet needs
@api_view(['POST'])
def save_user_request(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    serializer = UserRequestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(elevator=elevator)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#this updates elevator status whether it is working or not.
@api_view(['PUT'])
def update_elevator_status(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.running = False
    elevator.save()
    return Response({'message': 'Elevator not working'}, status=status.HTTP_200_OK)

#this opens door of elevator
@api_view(["POST"])
def open_door(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.door_status = 'open'
    elevator.save()
    return Response({'message': 'Elevator door opened'}, status=status.HTTP_200_OK)

#this close door of elevator
@api_view(['POST'])
def close_door(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.door_status = 'closed'
    elevator.save()
    return Response({'message': 'Elevator door closed'}, status=status.HTTP_200_OK)

#this forces elevator to move towards up direction 
@api_view(['POST'])
def move_elevator_up(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.current_floor += 1
    elevator.direction = 'up'
    elevator.save()
    return Response({'message': 'Elevator moving up'}, status=status.HTTP_200_OK)

#this ensure elevator to move down
@api_view(['POST'])
def move_elevator_down(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.current_floor -= 1
    elevator.direction = 'down'
    elevator.save()
    return Response({'message': 'Elevator moving down'}, status=status.HTTP_200_OK)

##this decieds to stop elevator
@api_view(['POST'])
def stop_elevator(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.direction = 'stop'
    elevator.save()
    return Response({'message': 'Elevator stopped'}, status=status.HTTP_200_OK)

#this make elevator is operational
@api_view(['POST'])
def mark_elevator_operational(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.operational = True
    elevator.save()
    return Response({'message': 'Elevator is operational'}, status=status.HTTP_200_OK)

#this make elevator is nonoperational
@api_view(['POST'])
def mark_elevator_non_operational(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.operational = False
    elevator.save()
    return Response({'message': 'Elevator is non-operational'}, status=status.HTTP_200_OK)
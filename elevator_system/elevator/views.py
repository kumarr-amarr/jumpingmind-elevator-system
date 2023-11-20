from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from.models import Elevator, UserRequest
from .serializers import UserRequestSerializer

@api_view(['POST'])
def initialize_elevator_system(request):
    try:
        num_elevators = int(request.data.get('num_elevators', 0))
    except ValueError:
        return Response({'error': 'Invalid number of elevators. Must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)

    if num_elevators <= 0:
        return Response({'error': 'Invalid number of elevators'}, status=status.HTTP_400_BAD_REQUEST)

    for i in range(1, num_elevators + 1):
        Elevator.objects.create(elevator_id=i, current_floor=1)

    return Response({'message': f'{num_elevators} elevators initialized successfully'}, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def open_door(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.door_status = 'open'
    elevator.save()
    return Response({'message': 'Elevator door opened'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def close_door(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.door_status = 'closed'
    elevator.save()
    return Response({'message': 'Elevator door closed'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def move_elevator_up(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.current_floor += 1
    elevator.direction = 'up'
    elevator.save()
    return Response({'message': 'Elevator moving up'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def move_elevator_down(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.current_floor -= 1
    elevator.direction = 'down'
    elevator.save()
    return Response({'message': 'Elevator moving down'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def stop_elevator(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.direction = 'stop'
    elevator.save()
    return Response({'message': 'Elevator stopped'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_user_request(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    serializer = UserRequestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(elevator=elevator)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetch_requests_for_elevator(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    requests = UserRequest.objects.filter(elevator=elevator)
    serializer = UserRequestSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_elevator_status(request):
    elevator_id = request.data.get('elevator_id')
    elevator = get_object_or_404(Elevator, elevator_id=elevator_id)
    elevator.running = False
    elevator.save()
    return Response({'message': 'Elevator marked as not working'}, status=status.HTTP_200_OK)

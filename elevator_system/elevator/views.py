from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from.models import Elevator

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
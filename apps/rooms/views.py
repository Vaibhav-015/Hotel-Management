from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RoomSerializer
from .models import Rooms

from drf_yasg.utils import swagger_auto_schema

# Create your views here.

@swagger_auto_schema(
    method='post',
    request_body=RoomSerializer,
    responses={201: RoomSerializer}
)
@api_view(['POST'])
def add_room(request):

    serializer = RoomSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    room_no = serializer.validated_data.get("room_no")
    room_capacity = serializer.validated_data.get("room_capacity")
    room_type = serializer.validated_data.get("room_type")
    room_price = serializer.validated_data.get("room_price")
    room_status = serializer.validated_data.get("room_status")

    qs = Rooms.objects.create(
        room_no=room_no,
        room_capacity=room_capacity,
        room_type=room_type,
        room_price=room_price,
        room_status=room_status
    )

    return Response(
        {
            "message": "Room added successfully",
            "status": status.HTTP_201_CREATED
        },
        status=status.HTTP_201_CREATED
    )

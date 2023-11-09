from rest_framework import viewsets

from management.models import Hotel, RoomType, Amenity, Room
from management.serializer import HotelSerializer, RoomTypeSerializer, AmenitySerializer, RoomReadSerializer, \
    RoomWriteSerializer
from rest_framework.permissions import IsAdminUser, AllowAny


# Create your views here.

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.order_by('-pk')
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUser]


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.order_by('-pk')
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAdminUser]


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.order_by('-pk')
    serializer_class = AmenitySerializer
    permission_classes = [IsAdminUser]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.order_by('-pk')
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return RoomWriteSerializer
        return RoomReadSerializer

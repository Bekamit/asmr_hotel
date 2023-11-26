from rest_framework import viewsets

from management.models import Hotel, RoomType, Equipment
from management.serializer import HotelWriteSerializer, RoomTypeSerializer, EquipmentSerializer, HotelReadSerializer
from rest_framework.permissions import IsAdminUser


# Create your views here.

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.order_by('pk')
    write_serializer_class = HotelWriteSerializer
    read_serializer_class = HotelReadSerializer
    # serializer_class = HotelWriteSerializer
    # permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        serializer_action_mapping = {
            'create': self.write_serializer_class,
            'update': self.write_serializer_class,
            'partial_update': self.write_serializer_class
        }

        return serializer_action_mapping.get(
            self.action,
            self.read_serializer_class,
        )


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.order_by('pk')
    serializer_class = RoomTypeSerializer
    # permission_classes = [IsAdminUser]


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.order_by('pk')
    serializer_class = EquipmentSerializer
    # permission_classes = [IsAdminUser]


# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.order_by('-pk')
#     serializer_class = RoomSerializer
#     permission_classes = [AllowAny]
#
#     def get_serializer_class(self):
#         if self.action == 'create':
#             return RoomWriteSerializer
#         return super().get_serializer_class()
#     # def get_serializer_class(self):
#     #     if self.action == 'create':
#     #         return RoomWriteSerializer
#     #     return RoomReadSerializer

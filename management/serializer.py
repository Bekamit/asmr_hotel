from rest_framework import serializers

from management.models import Hotel, RoomType, Equipment, Room, Amenity
from drf_writable_nested.serializers import WritableNestedModelSerializer


class AmenityWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        exclude = ['room']


class RoomWriteSerializer(WritableNestedModelSerializer):
    # hotel = HotelSerializer()
    # type = RoomTypeSerializer()
    amenities = AmenityWriteSerializer(many=True)

    class Meta:
        model = Room
        exclude = ['hotel', 'equipments']
        # fields = '__all__'


class HotelWriteSerializer(WritableNestedModelSerializer):
    rooms = RoomWriteSerializer(many=True)

    class Meta:
        model = Hotel
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class AmenityReadSerializer(AmenityWriteSerializer):
    equipment = EquipmentSerializer()


class RoomReadSerializer(RoomWriteSerializer):
    amenities = AmenityReadSerializer(many=True)


class HotelReadSerializer(HotelWriteSerializer):
    rooms = RoomReadSerializer(many=True)


# class HotelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Hotel
#         fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

# class RoomWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = '__all__'


# class RoomSerializer(serializers.ModelSerializer):
#     # hotel = HotelSerializer()
#     # type = RoomTypeSerializer()
#
#     class Meta:
#         model = Room
#         fields = '__all__'

from django.contrib import admin

from management.models import Hotel, RoomType, Amenity, Room, RoomAmenity

# Register your models here.

admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(Amenity)
admin.site.register(Room)
admin.site.register(RoomAmenity)

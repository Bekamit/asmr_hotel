from django.contrib import admin

from management.models import Hotel, RoomType, Equipment, Room, Amenity

# Register your models here.

admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(Equipment)
admin.site.register(Room)
admin.site.register(Amenity)

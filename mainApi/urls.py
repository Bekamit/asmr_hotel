from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from management.views import HotelViewSet, RoomTypeViewSet, AmenityViewSet, RoomViewSet
from my_auth.views import UserViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('hotels', HotelViewSet)
router.register('room-type', RoomTypeViewSet)
router.register('amenities', AmenityViewSet)
router.register('rooms', RoomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]

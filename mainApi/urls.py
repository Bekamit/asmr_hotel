from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

from management.views import HotelViewSet, RoomTypeViewSet, EquipmentViewSet
from my_auth.views import UserViewSet

from drf_spectacular.views import SpectacularJSONAPIView, SpectacularSwaggerView


router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('hotels', HotelViewSet)
router.register('room-type', RoomTypeViewSet)
router.register('equipments', EquipmentViewSet)
# router.register('rooms', RoomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('schema/', SpectacularJSONAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

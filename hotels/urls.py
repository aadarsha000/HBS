from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AdminHotelViewSet, HotelViewSet

router = DefaultRouter()
router.register("api/hotels", HotelViewSet, basename="hotels")
router.register("api/admin/hotels", AdminHotelViewSet, basename="admin_hotels")

urlpatterns = [
    path("", include(router.urls)),
]

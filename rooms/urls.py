from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RoomViewSet, RoomTypeViewSet, AdminRoomViewSet, AdminRoomTypeViewSet

router = DefaultRouter()
router.register("api/rooms", RoomViewSet, basename="rooms")
router.register("api/room-types", RoomTypeViewSet, basename="room-types")
router.register("api/admin/rooms", AdminRoomViewSet, basename="admin-rooms")
router.register(
    "api/admin/room-types", AdminRoomTypeViewSet, basename="admin-room-types"
)

urlpatterns = [path("", include(router.urls))]

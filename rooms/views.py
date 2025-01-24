from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAdminUser

from .models import Room, RoomTypes
from .serializers import RoomSerializer, RoomTypeSerializer
from .filters import RoomFilter


class AdminRoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]


class AdminRoomTypeViewSet(ModelViewSet):
    queryset = RoomTypes.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAdminUser]


class RoomTypeViewSet(ReadOnlyModelViewSet):
    queryset = RoomTypes.objects.all()
    serializer_class = RoomTypeSerializer


class RoomViewSet(ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filterset_class = RoomFilter

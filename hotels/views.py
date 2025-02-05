from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import HotelSerializer, CreateHotelSerializer
from .models import Hotel
from .filters import HotelFilter


class AdminHotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    filterset_class = HotelFilter

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return CreateHotelSerializer
        return HotelSerializer


class HotelViewSet(ReadOnlyModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filterset_class = HotelFilter

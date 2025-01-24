from rest_framework import serializers

from .models import Room, RoomTypes, RoomImages
from hotels.serializers import HotelSerializer


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImages
        fields = "__all__"


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTypes
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True)
    room_type = RoomTypeSerializer()
    hotel = HotelSerializer()

    class Meta:
        model = Room
        fields = "__all__"

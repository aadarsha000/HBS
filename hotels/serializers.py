from rest_framework import serializers

from .models import Hotel, HotelImage


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    images = HotelImageSerializer(many=True)

    class Meta:
        model = Hotel
        fields = "__all__"

from rest_framework import serializers

from .models import Hotel, HotelImage


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = "__all__"


class CreateHotelSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.FileField(), required=False, write_only=True
    )

    class Meta:
        model = Hotel
        fields = "__all__"

    def create(self, validated_data):
        images = validated_data.pop("images", [])
        hotel = super().create(validated_data)

        # Handle Many-to-Many relation with HotelImage
        hotel_image_instances = [
            HotelImage.objects.create(image=image) for image in images
        ]
        hotel.images.set(hotel_image_instances)
        return hotel

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["images"] = HotelImageSerializer(instance.images.all(), many=True).data
        return data


class HotelSerializer(serializers.ModelSerializer):
    images = HotelImageSerializer(many=True)

    class Meta:
        model = Hotel
        fields = "__all__"

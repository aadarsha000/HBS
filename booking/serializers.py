from rest_framework import serializers

from rooms.serializers import RoomSerializer
from .models import Booking
from accounts.serializers import UserSerializer


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        extra_kwargs = {"user": {"required": False}}


class ReadBookingSerializers(serializers.ModelSerializer):
    room = RoomSerializer()
    user = UserSerializer()

    class Meta:
        model = Booking
        fields = "__all__"


class StripeSerializer(serializers.Serializer):
    paymentIntentId = serializers.CharField(required=True)
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), required=True
    )

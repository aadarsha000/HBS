import stripe

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ReadBookingSerializers, BookingSerializers, StripeSerializer
from .models import Booking
from payments.models import PaymentHistory
from shared.custom_response import SuccessResponse, FailedResponse

# Create your views here.


class UserBookingView(ModelViewSet):
    serializer_class = BookingSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return BookingSerializers
        return ReadBookingSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdminBookingView(ModelViewSet):
    serializer_class = BookingSerializers
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return BookingSerializers
        return ReadBookingSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserCreateStripePaymentIntent(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, booking_id):
        try:
            user = request.user
            booking = Booking.objects.get(
                user=user, id=booking_id, status=Booking.STATUS.PENDING
            )
            amount = int(booking.total * 100)
            payment_intent = stripe.PaymentIntent.create(
                description=f"Purchasing book from Upschool",
                shipping={
                    "name": f"{user.first_name} {user.last_name}",
                    "address": {
                        "line1": booking.address_line_1,
                        "postal_code": booking.postal_code,
                        "city": booking.city,
                        "state": booking.state,
                        "country": booking.country,
                    },
                },
                amount=amount,
                currency="usd",
                payment_method_types=["card"],
            )
            return SuccessResponse(
                message="Client Secret",
                data={"client_secret": payment_intent.client_secret},
            )
        except Exception as e:
            FailedResponse(message=str(e))


class UserCheckStripePaymentStatus(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            serializer = StripeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            paymentIntentId = serializer.validated_data["paymentIntentId"]
            booking = serializer.validated_data["booking_id"]
            payment_intent = stripe.PaymentIntent.retrieve(paymentIntentId)
            payment_status = payment_intent.status
            if payment_status == "succeeded":
                booking.status = Booking.STATUS.SUCCESS
                booking.save()
                PaymentHistory(booking=booking, customer=user, amount=booking.total)
                return SuccessResponse
        except Exception as e:
            FailedResponse(message=str(e))

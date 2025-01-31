from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AdminBookingView,
    UserBookingView,
    UserCheckStripePaymentStatus,
    UserCreateStripePaymentIntent,
)

router = DefaultRouter()
router.register("api/bookings", UserBookingView, basename="bookings")
router.register("api/admin/bookings", AdminBookingView, basename="admin_bookings")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "create-stripe-payment-intent/<int:booking_id>/",
        UserCreateStripePaymentIntent.as_view(),
    ),
    path(
        "check-stripe-payment/",
        UserCheckStripePaymentStatus.as_view(),
    ),
]

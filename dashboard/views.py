from rest_framework.views import APIView

from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncMonth


from hotels.models import Hotel
from rooms.models import Room
from booking.models import Booking
from accounts.models import User

from shared.custom_response import SuccessResponse, FailedResponse

from calendar import month_abbr


class DashboardStats(APIView):

    def get(self, request):
        try:
            today = timezone.now().date()

            # Fetch total counts
            total_no_of_hotels = Hotel.objects.count()
            total_no_of_rooms = Room.objects.count()
            total_booked_room = Booking.objects.filter(check_in_date__gte=today).count()
            total_bookings_today = Booking.objects.filter(check_in_date=today).count()
            new_booking_today = Booking.objects.filter(created_at__date=today).count()

            # Fetch bookings grouped by month
            bookings_per_month = (
                Booking.objects.annotate(month=TruncMonth("check_in_date"))
                .values("month")
                .annotate(total=Count("id"))
                .order_by("month")
            )

            # Create a dictionary with all months initialized to 0
            monthly_bookings = {month_abbr[i]: 0 for i in range(1, 13)}

            # Populate the dictionary with actual booking data
            for entry in bookings_per_month:
                month_name = entry["month"].strftime("%b")
                monthly_bookings[month_name] = entry["total"]

            total_customer = User.objects.filter(role=User.Roles.CUSTOMER).count()
            new_customer = User.objects.filter(
                role=User.Roles.CUSTOMER, date_joined__date=today
            ).count()
            return SuccessResponse(
                message="Dashboard Stats",
                data={
                    "total_no_of_hotels": total_no_of_hotels,
                    "total_no_of_rooms": total_no_of_rooms,
                    "total_booked_room": total_booked_room,
                    "total_bookings_today": total_bookings_today,
                    "new_booking_today": new_booking_today,
                    "bookings_per_month": monthly_bookings,
                    "total_customer": total_customer,
                    "new_customer": new_customer,
                },
            )
        except Exception as e:
            return FailedResponse(message=str(e))

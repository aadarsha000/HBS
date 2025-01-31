from django.db import models

from shared.abstract_base_model import AbstractBaseModel
from booking.models import Booking
from accounts.models import User


# Create your models here.
class PaymentHistory(AbstractBaseModel):
    class PaymentMethod(models.TextChoices):
        ONLINE = "online", "Online"
        CASH = "cash", "Cash"

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=4, max_digits=19, default=0)

    class Meta:
        db_table = "payment_history"

from django.db import models

from shared.abstract_base_model import AbstractBaseModel
from accounts.models import User
from rooms.models import Room


# Create your models here.
class Booking(AbstractBaseModel):
    class STATUS(models.TextChoices):
        SUCCESS = "success", "Success"
        FAILED = "failed", "Failed"
        PENDING = "pending", "Pending"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    country = models.CharField(max_length=255, null=True, blank=True)
    address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    total = models.DecimalField(decimal_places=4, max_digits=19, default=0)
    status = models.CharField(
        max_length=20, choices=STATUS.choices, default=STATUS.PENDING
    )

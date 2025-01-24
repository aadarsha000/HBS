from django.db import models


from shared.abstract_base_model import AbstractBaseModel
from hotels.models import Hotel
from shared.file_utils import file_upload_path, validate_five_mb_image_size


# Create your models here.
class RoomImages(AbstractBaseModel):
    image = models.ImageField(
        upload_to=file_upload_path,
        validators=[validate_five_mb_image_size],
    )


class RoomTypes(AbstractBaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to=file_upload_path,
        validators=[validate_five_mb_image_size],
    )

    class Meta:
        db_table = "room_types"


class Room(AbstractBaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomTypes, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_beds = models.PositiveBigIntegerField()
    total_capacity = models.PositiveBigIntegerField()
    images = models.ManyToManyField(RoomImages, related_name="hotels")

    class Meta:
        db_table = "rooms"

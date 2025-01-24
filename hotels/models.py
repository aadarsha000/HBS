from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from shared.abstract_base_model import AbstractBaseModel
from shared.file_utils import file_upload_path, validate_five_mb_image_size


# Create your models here.
class HotelImage(AbstractBaseModel):
    image = models.ImageField(
        upload_to=file_upload_path,
        validators=[validate_five_mb_image_size],
    )


class Hotel(AbstractBaseModel):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ManyToManyField(HotelImage, related_name="hotels")
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0
    )

    class Meta:
        db_table = "hotels"
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"

    def __str__(self):
        return self.name

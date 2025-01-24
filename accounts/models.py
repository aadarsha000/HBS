from django.db import models
from django.contrib.auth.models import AbstractUser

from shared.file_utils import file_upload_path, validate_one_mb_image_size

# Create your models here.


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "admin", "Admin"
        STAFF = "staff", "Staff"
        CUSTOMER = "customer", "Customer"

    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        OTHERS = "others", "Others"

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10, choices=Roles.choices, default=Roles.CUSTOMER
    )
    avatar = models.ImageField(
        upload_to=file_upload_path,
        validators=[validate_one_mb_image_size],
        blank=True,
        null=True,
    )
    gender = models.CharField(
        max_length=10, choices=Gender.choices, blank=True, null=True
    )
    country = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = "users"

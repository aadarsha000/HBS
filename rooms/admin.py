from django.contrib import admin

from .models import Room, RoomImages, RoomTypes

# Register your models here.

admin.site.register(Room)

admin.site.register(RoomTypes)

admin.site.register(RoomImages)

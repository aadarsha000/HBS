from django.contrib import admin

from .models import Hotel, HotelImage

# Register your models here.


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "location", "rating"]


admin.site.register(HotelImage)

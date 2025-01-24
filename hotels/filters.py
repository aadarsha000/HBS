import django_filters
from django.db import models

from .models import Hotel


class HotelFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="Search",
    )

    class Meta:
        model = Hotel
        fields = {
            "name": ["icontains"],
            "location": ["icontains"],
            "rating": ["gte", "lte", "exact"],
        }

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__icontains=value) | models.Q(location__icontains=value)
        )

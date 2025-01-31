import django_filters
from django.db import models

from ..models import Room


class RoomFilters(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="Search",
    )

    class Meta:
        model = Room
        fields = {
            "name": ["icontains"],
            "hotel": ["exact"],
            "room_type": ["exact"],
            "price": ["gte", "lte", "exact"],
        }

    def filter_search(self, queryset, name, value):
        return queryset.filter(models.Q(name__icontains=value))

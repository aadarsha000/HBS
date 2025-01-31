import django_filters
from django.db import models

from ..models import RoomTypes


class RoomTypesFilters(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="Search",
    )

    class Meta:
        model = RoomTypes
        fields = {
            "name": ["icontains"],
        }

    def filter_search(self, queryset, name, value):
        return queryset.filter(models.Q(name__icontains=value))

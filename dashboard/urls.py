from django.urls import path

from .views import DashboardStats

urlpatterns = [path("api/stats/", DashboardStats.as_view())]

from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import CustomRegisterAPIView, CustomLoginAPIView, PasswordChangeAPIView

urlpatterns = [
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register/", CustomRegisterAPIView.as_view(), name="register"),
    path("api/login/", CustomLoginAPIView.as_view(), name="login"),
    path(
        "api/password-change/", PasswordChangeAPIView.as_view(), name="password-change"
    ),
]

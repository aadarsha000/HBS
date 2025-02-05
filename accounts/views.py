from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

from shared.custom_response import SuccessResponse, FailedResponse
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    PasswordChangeSerializer,
)


# Create your views here.
class CustomRegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            # user_data = self.get_serializer(user).data
            return SuccessResponse(
                message="User registered successfully",
                data=[],
            )
        except ValidationError as e:
            return FailedResponse(message=serializer.errors)
        except Exception as e:
            return FailedResponse(message=str(e))


class CustomLoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            user_data = UserSerializer(user).data
            refresh = RefreshToken.for_user(user)
            return SuccessResponse(
                message="User logged in SuccessfullY.",
                data={
                    "user": user_data,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
            )
        except ValidationError as e:
            return FailedResponse(message=serializer.errors)
        except Exception as e:
            return FailedResponse(message=str(e))


class PasswordChangeAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PasswordChangeSerializer

    def post(self, request, format=None):
        try:
            user = self.request.user
            serializer = PasswordChangeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            old_password = serializer.validated_data["old_password"]
            new_password = serializer.validated_data["new_password"]
            auth_user = authenticate(
                request=request,
                username=user.username,
                password=old_password,
            )
            if auth_user:
                validate_password(new_password, user=user)
                user.set_password(new_password)
                user.save()
            else:
                return FailedResponse(message="Old password is incorrect")
            return SuccessResponse(message="Password changed successfully", data=[])
        except ValidationError as e:
            return FailedResponse(message=serializer.errors)
        except Exception as e:
            return FailedResponse(message=e)


class UserProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        try:
            user = request.user
            profile = UserSerializer(user)
            return SuccessResponse(
                message="Profile fetch successfully", data=profile.data
            )
        except Exception as e:
            return FailedResponse(message=e)

    def put(self, request):
        try:
            user = request.user
            profile = UserSerializer(instance=user, data=request.data, partial=True)
            if profile.is_valid():
                profile.save()
                return SuccessResponse(
                    message="Profile updated successfully", data=profile.data
                )
            else:
                return FailedResponse(message="Validation failed", data=profile.errors)
        except Exception as e:
            return FailedResponse(message=e)

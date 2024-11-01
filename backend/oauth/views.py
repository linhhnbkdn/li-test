from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.viewsets import GenericViewSet

from oauth.serializer.user_lite_serializer import UserLiteSerializer
from oauth.serializer.user_login_serializer import UserLoginSerializer


class AnonymousAuthView(GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def get_success_headers(self, data):
        try:
            return {"Location": str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    @action(detail=False, methods=["post"], url_path="login")
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["user_id"],
            password=serializer.validated_data["password"],
        )
        if not user:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if serializer.validated_data["remmber_me"]:
            # Set age of session to 1 month 60*60*24*30
            request.session.set_expiry(2592000)
        login(
            request,
            user,
            backend="django.contrib.auth.backends.ModelBackend",
        )
        headers = self.get_success_headers(serializer.data)
        response_data = UserLiteSerializer(user).data
        return Response(
            response_data,
            status=status.HTTP_200_OK,
            headers=headers,
        )


class UserAuthView(GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.Serializer

    def get_success_headers(self, data):
        try:
            return {"Location": str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    @action(detail=False, methods=["post"], url_path="logout")
    def logout(self, request, *args, **kwargs):
        logout(request)
        return Response(
            {"message": "Logout successful"},
            status=status.HTTP_200_OK,
        )

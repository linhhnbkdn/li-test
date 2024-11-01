from django.contrib.auth.models import User

from common.model_serializer_base import BaseModelSerializer


class UserLiteSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "date_joined"]

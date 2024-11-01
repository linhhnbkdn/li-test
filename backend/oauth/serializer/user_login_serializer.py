from rest_framework import serializers

from common.serializer_base import BaseSerializer


class UserLoginSerializer(BaseSerializer):
    user_id = serializers.CharField(
        required=True,
    )
    password = serializers.CharField(
        required=True,
    )
    remmber_me = serializers.BooleanField(
        required=False,
        default=False,
    )

    def create(self, validated_data):
        pass

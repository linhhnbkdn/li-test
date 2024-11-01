from rest_framework import serializers

from booking_app.models import PaymentModel
from common.serializer_base import BaseSerializer


def booking_id_validator(value):
    from booking_app.models.booking import BookingModel

    if not BookingModel.objects.filter(
        id=value,
        is_active=True,
        is_deleted=False,
    ).exists():
        raise ValueError(f"Booking with id {value} does not exist")


class PaymentSerializer(BaseSerializer):
    booking_id = serializers.IntegerField(
        validators=[booking_id_validator],
    )
    amount = serializers.FloatField()
    method = serializers.HiddenField(default="StripePaymentGateway")
    status = serializers.HiddenField(default="PENDING")

    class Meta:
        model = PaymentModel
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)

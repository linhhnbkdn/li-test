import logging

from rest_framework import serializers

from booking_app.models import SlotModel
from common.serializer_base import BaseSerializer

logger = logging.getLogger(__name__)


def validate_slot_id(value):
    if SlotModel.objects.filter(id=value, is_booked=True).exists():
        raise serializers.ValidationError("Slot does not exist or is not booked")

class BookingSerializer(BaseSerializer):
    slot_id = serializers.IntegerField(
        validators=[validate_slot_id],
    )
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

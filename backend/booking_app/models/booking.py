import logging
from typing import Any

from django.db import models

from common.model_orm_base import BaseModel

logger = logging.getLogger(__name__)


class BookingModel(BaseModel):
    slot_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = False
        db_table = "booking"
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"{self.slot_id} - {self.user_id}"

    def __repr__(self):
        return f"{self.slot_id} - {self.user_id}"

import json

from django.db import transaction

from booking_app.models import BookingModel, SlotModel
from worker.base_task import CeleryTaskABC
from worker.config import app


@app.task(
    bind=True,
    base=CeleryTaskABC,
    name="execute_booking_creating_event",
)
def execute_booking_creating_event(self, data: json) -> None:
    with transaction.atomic():
        slot_id = data["slot_id"]
        SlotModel.objects.get(id=slot_id).update(is_booked=True)
        BookingModel.objects.create(**data)

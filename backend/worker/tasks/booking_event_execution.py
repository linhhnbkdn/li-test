import json

from booking_app.models import BookingModel
from worker.base_task import CeleryTaskABC
from worker.config import app


@app.task(
    bind=True,
    base=CeleryTaskABC,
    name="execute_booking_creating_event",
)
def execute_booking_creating_event(self, data: json) -> None:
    BookingModel.objects.create(**data)

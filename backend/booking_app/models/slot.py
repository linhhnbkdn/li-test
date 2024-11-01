from django.db import models

from common.model_orm_base import BaseModel


class SlotModel(BaseModel):
    pduct_id = models.BigIntegerField()
    no = models.IntegerField()
    is_booked = models.BooleanField(default=False)

    class Meta:
        abstract = False
        db_table = "slot"
        verbose_name = "Slot"
        verbose_name_plural = "Slots"

    def __str__(self):
        return f"{self.pduct_id} - {self.no}"

    def __repr__(self):
        return f"{self.pduct_id} - {self.no}"

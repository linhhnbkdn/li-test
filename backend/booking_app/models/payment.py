from django.db import models

from common.model_orm_base import BaseModel


class PaymentModel(BaseModel):
    booking_id = models.BigIntegerField()
    amount = models.FloatField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    method = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        abstract = False
        db_table = "payment"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"{self.booking_id} - {self.amount}"

    def __repr__(self):
        return f"{self.booking_id} - {self.amount}"

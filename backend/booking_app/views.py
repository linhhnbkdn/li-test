import time
from typing import Any

import redis
from django.conf import settings
from injector import inject
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins

from booking_app.serializer.booking_serializer import BookingSerializer
from booking_app.serializer.payment_serializer import PaymentSerializer
from third_party.payment.payment_abc import PaymentGateway
from worker.tasks import execute_booking_creating_event

KEY_SLOT_PRODUCT_REDIS_LOCK = "{slot}"
TIMMING_LOCK = 100

redis_instance = redis.StrictRedis.from_url(settings.CACHES["default"]["LOCATION"])


class BookingViewSet(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["user_id"] = self.request.user.id
        # Atomic operation to lock the slot
        lock_key = KEY_SLOT_PRODUCT_REDIS_LOCK.format(slot=request.data["slot_id"])
        lock_acquired = redis_instance.setnx(lock_key, int(time.time()) + TIMMING_LOCK)
        if not lock_acquired:
            return Response(
                {"message": "Slot is locked, please try again later"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Push event to worker
        execute_booking_creating_event.apply_async(
            args=(serializer.validated_data,),
        )
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class PaymentViewSet(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer

    @inject
    def setup(self, request, payment_gateway: PaymentGateway, **kwargs) -> None:
        self.payment_gateway = payment_gateway

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.payment_gateway.process_payment(
            serializer.validated_data["amount"],
            "usb",
        )
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

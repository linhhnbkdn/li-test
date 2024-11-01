import logging

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from booking_app.models import BookingModel, ProductModel, SlotModel

logger = logging.getLogger("backend.command")


class Command(BaseCommand):
    help = "Import seed data"

    def handle(self, *args, **options):
        logger.info("Importing seed data")
        self.delete_all()
        user = User.objects.create_user(
            username="admin",
            email="admin@admin.com",
            password="admin",
            is_superuser=True,
            is_staff=True,
        )
        pduct = ProductModel.objects.create(
            name="Product 1",
            price=1000,
            description="Product 1 description",
        )
        slot_1 = SlotModel.objects.create(
            pduct_id=pduct.id,
            no=1,
        )
        SlotModel.objects.create(
            pduct_id=pduct.id,
            no=1,
        )
        BookingModel.objects.create(
            slot_id=slot_1.id,
            user_id=user.id,
        )
        logger.info("Seed data imported")

    def delete_all(self):
        logger.info("Deleting all seed data")
        BookingModel.objects.all().delete()
        SlotModel.objects.all().delete()
        ProductModel.objects.all().delete()
        User.objects.all().delete()
        logger.info("All seed data deleted")

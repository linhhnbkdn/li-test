import os

from celery import Celery
from django.conf import settings


def set_django_settings_module() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")


set_django_settings_module()
app = Celery(
    "worker",
    broker=settings.BROKER_URL,
    include=["worker.tasks"],
)

# See: https://docs.celeryproject.org/en/stable/userguide/configuration.html
app.conf.update(
    broker_transport_options={
        "region": "ap-northeast-1",
        "wait_time_seconds": 15,
        "sts_token_timeout": 43200,
    },
)

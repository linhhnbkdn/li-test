import celery


class CeleryTaskABC(celery.Task):  # type: ignore
    client_error_exceptions = ()
    autoretry_for = (Exception,)
    max_retries = 3
    retry_backoff = 5
    retry_jitter = False
    acks_late = True
    acks_on_failure_or_timeout = True
    retry_backoff_max = 80
    trail = True

    def __init__(self, *args, **kwargs):  # type: ignore
        super().__init__(*args, **kwargs)

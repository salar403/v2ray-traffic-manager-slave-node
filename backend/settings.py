import sentry_sdk
from pathlib import Path
from sentry_sdk.integrations.django import DjangoIntegration
from backend.environments import (
    REDIS_HOST,
    REDIS_PORT,
    REDIS_CELERY_BACKEND,
    REDIS_CELERY_BROKER,
    SENTRY_DSN_ADDRESS,
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-@+3x_)p+mox=o_ne0a)-0+tkdwzr%l5o8dmek0j$)v4ffsk%hs"

DEBUG = False

INSTALLED_APPS = ["traffic"]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_BROKER}"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_BACKEND}"
CELERY_BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 31540000}
CELERY_CREATE_MISSING_QUEUES = True


# sentry_sdk.init(dsn=SENTRY_DSN_ADDRESS, integrations=[DjangoIntegration()])


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "INFO"},
    },
}

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.result_expires = 180

app.conf.beat_schedule = {
    # "update_traffic_usages": {
    #     "task": "traffic.tasks.retrieve_traffic",
    #     "schedule": 1.0,
    #     "options": {"queue": "main"},
    # },
}

app.conf.timezone = "UTC"
app.autodiscover_tasks()

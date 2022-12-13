from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-@+3x_)p+mox=o_ne0a)-0+tkdwzr%l5o8dmek0j$)v4ffsk%hs"

DEBUG = False

INSTALLED_APPS = ["traffic"]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

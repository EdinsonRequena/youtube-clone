from .base import *  # pylint: disable=wildcard-import,unused-wildcard-import

DEBUG = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
INTERNAL_IPS = ["127.0.0.1"]

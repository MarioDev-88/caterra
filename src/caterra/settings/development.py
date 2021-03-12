
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += (
    "debug_toolbar",
)

ALLOWED_HOSTS = [
    "165.232.133.76",
    "localhost",
    "127.0.0.1"
]

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

# Email settings
EMAIL_HOST = "smtp.mailtrap.io"
EMAIL_HOST_USER = "63b98ec87849b2"
EMAIL_HOST_PASSWORD = "39274699e31ab0"
EMAIL_PORT = "2525"

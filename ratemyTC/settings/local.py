from .base import *
from .base import env


# Importing all the base settings


SECRET_KEY = env(
    "SECRET_KEY",
    default="_wUMlJA3elxV3wC6ouaWPm-zuB4ugwVBcoDH5tIBBhQ",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]

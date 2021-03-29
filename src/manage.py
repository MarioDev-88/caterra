#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import load_dotenv

env = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), ".env")

load_dotenv(dotenv_path=env)


def main():
    if os.environ.get("ENV") == "production":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "caterra.settings.production")
    elif os.environ.get("ENV") == "development":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "caterra.settings.development")
    else:
        sys.exit("No ENV variable configured.")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

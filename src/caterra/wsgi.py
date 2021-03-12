import os

import dotenv
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

env = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), ".env")

load_dotenv(dotenv_path=env)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "caterra.settings.production")

application = get_wsgi_application()

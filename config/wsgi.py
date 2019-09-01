"""
WSGI config for testt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import environ
from django.core.wsgi import get_wsgi_application

ROOT_DIR = environ.Path(__file__) - 2
env = environ.Env()
env.read_env(str(ROOT_DIR.path('.env')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", env('DJANGO_SETTINGS_MODULE'))

application = get_wsgi_application()

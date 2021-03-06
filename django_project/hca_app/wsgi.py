"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hca_app.settings")

application = get_wsgi_application()

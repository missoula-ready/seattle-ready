"""
WSGI config for disasterinfosite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
os.environ["DJANGO_SETTINGS_MODULE"] = "disasterinfosite.settings"
sys.path.append('/home/missoulaready/seattle-ready/venv/lib/python3.5/site-packages')
sys.path.append('/home/missoulaready/seattle-ready')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

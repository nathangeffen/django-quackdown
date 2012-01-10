import os, sys

sys.path.append('/home/nathan/programming/django-quackdown/')
sys.path.append('/home/nathan/programming/django-pubman')
sys.path.append('/home/nathan/programming/django-siteconfig')
os.environ['DJANGO_SETTINGS_MODULE'] = 'quackdownproject.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()


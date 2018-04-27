from .base import *
import os
import django_heroku

DEBUG = False
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
django_heroku.settings(locals())

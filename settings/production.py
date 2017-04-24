from settings.common_es_mx import *

WSGI_APPLICATION = 'wsgi.production.application'

DEBUG = False
ALLOWED_HOSTS = ['*']

STATIC_ROOT = "/var/www/example.com/static/"
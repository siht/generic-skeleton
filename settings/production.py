from common_es_mx import *

WSGI_APPLICATION = 'wsgi.production.wsgi.application'

DEBUG = False
ALLOWED_HOSTS = ['*']

STATIC_ROOT = "/var/www/example.com/static/"
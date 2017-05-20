# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from settings.common_es_mx import *

WSGI_APPLICATION = 'wsgi.preproduction.application'

DEBUG = False
ALLOWED_HOSTS = ['*']

STATIC_ROOT = "/var/www/example.com/static/"

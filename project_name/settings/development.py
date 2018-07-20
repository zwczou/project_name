# -*- coding: utf-8 -*-


import os

from .base import *


DEBUG = True

INTERNAL_IPS = ['127.0.0.1']

SECRET_KEY = 'secret'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from local_settings import *
except ImportError:
    pass

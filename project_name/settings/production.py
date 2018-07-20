# -*- coding: utf-8 -*-


import os

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

# NOTIFICATIONS
# A tuple that lists people who get code error notifications.
ADMINS = (
    ('zwczou', 'zwczou@gmail.com'),
)
MANAGERS = ADMINS

try:
    from local_settings import *
except ImportError:
    pass

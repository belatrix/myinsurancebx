"""
Set this environment variable
DJANGO_SETTINGS_MODULE=MyInsurance.settings.local
"""

from .base import *  # noqa: F403


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r#pywl@585e)(5&lo2+j1x9$7stb^q3#p@##xv@yc1c5=vwzyr'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

ALLOWED_HOSTS = ['127.0.0.1']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}

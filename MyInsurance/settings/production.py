"""
Set this environment variable
DJANGO_SETTINGS_MODULE=MyInsurance.settings.production
"""

import dj_database_url
import django_heroku
from .base import *  # noqa: F403,F401
from utils.environment import env


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', '')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

ALLOWED_HOSTS = ['.herokuapp.com']


# Production apps
PRODUCTION_ONLY_APPS = [
    'storages',
]

INSTALLED_APPS = INSTALLED_APPS + PRODUCTION_ONLY_APPS

# Configure Django App for Heroku
django_heroku.settings(locals())


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)  # noqa: F405

# AWS
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', '')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', '')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME)
AWS_S3_OBJECTS_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = 'public-read'

# Storage settings
DEFAULT_FILE_STORAGE = 'MyInsurance.settings.storage_backends.MediaStorage'
"""
Django settings for portfolio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u#qs750ih@ntq81koohf3*g6%34$a-tlu(ki-(jp5srz5l*3rp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config(default='postgres://127.0.0.1:5432/kennethroraback')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


import os
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir))

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'storages',
)

LOCAL_APPS = (
    'projects',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

ROOT_URLCONF = 'portfolio.urls'

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

if os.environ.get('DJANGO_PRODUCTION'):
    print "I think I'm a production environment"
    # ENVIRONMENT = 'PRODUCTION'
    # DEBUG = False
    DEFAULT_FILE_STORAGE = 'portfolio.s3utils.MediaS3BotoStorage'
    STATICFILES_STORAGE = 'portfolio.s3utils.StaticS3BotoStorage'

    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET', 'kennethroraback')
    S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
    MEDIA_DIRECTORY = '/media/'
    STATIC_DIRECTORY = '/static/'
    STATIC_URL = S3_URL + STATIC_DIRECTORY
    MEDIA_URL = S3_URL + MEDIA_DIRECTORY
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

else:
    MEDIA_DIRECTORY = '/media/'
    STATIC_DIRECTORY = '/static/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
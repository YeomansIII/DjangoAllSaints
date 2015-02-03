"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Production / development switches
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

SECRET_KEY = '{{ secret_key }}'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blanc_basic_assets',
    'blanc_basic_news',
    'mptt',
    'django_mptt_admin',
    'blanc_basic_pages',
    'blanc_basic_events',
    'easy_thumbnails',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blanc_basic_pages.middleware.PageFallbackMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}


# Caches
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/London'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'theme/static'),
)


# File uploads
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#file-uploads

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Templates
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#templates

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '{{ project_name }}/templates'),
    os.path.join(BASE_DIR, 'theme/templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


# Logging
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/logging/#configuring-logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}


# Any other application config goes below here

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# S3 file storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False
GZIP_CONTENT_TYPES = ()

# Thumbnail generation
THUMBNAIL_SUBDIR = 'thumbs'
THUMBNAIL_PRESERVE_EXTENSIONS = ('png',)
THUMBNAIL_QUALITY = 100
THUMBNAIL_DEFAULT_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

## Django Church applications
# - Change the uncommented sections
# - Change commented sections from default values if needed

## Pages
# PAGE_TEMPLATES = (
#     ('', 'Default'),
# )
# PAGE_SHOW_LOGIN = False

## News
NEWS_TITLE = 'My Church'
#NEWS_PER_PAGE = 10
#NEWS_FEED_LIMIT = 10

# Calendar
EVENTS_CALENDAR_NAME = 'My Church'
# EVENTS_CALENDAR_DESCRIPTION = 'Events Calendar'
# EVENTS_START_SUNDAY = True

# Local settings override
try:
    from local_settings import *
except ImportError:
    pass

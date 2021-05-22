
import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# PROJECT IMPORTS
from heartcare.local_settings import (
    SECRET_KEY, TEMPLATES_DIR, STATICFILES_DIR, STATIC_DIR, MEDIA_DIR,
    LOGS_DIR, DEBUG, ENABLE_HTTPS, ALLOWED_HOSTS, INTERNAL_IPS, DB_CONFIG,
    CELERY_BROKER_URL, CELERY_RESULT_BACKEND, CELERY_CACHE_BACKEND,
    CORS_ALLOWED_ORIGINS
)

from heartcare.logging import LOGGING
# from heartcare.juzzmin import CONFIG

PROJECT_NAME = 'Patient-Management-System'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...) -------
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SETTINGS_DIR)
TEMPLATES_DIR = os.getenv('TEMPLATES_DIR', TEMPLATES_DIR)
STATICFILES_DIR = os.getenv('STATICFILES_DIR', STATICFILES_DIR)
STATIC_DIR = os.getenv('STATIC_DIR', STATIC_DIR)
MEDIA_DIR = os.getenv('MEDIA_DIR', MEDIA_DIR)
LOGS_DIR = os.getenv('LOGS_DIR', LOGS_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', DEBUG)

ALLOWED_HOSTS = ALLOWED_HOSTS


if ENABLE_HTTPS:  # local_settings
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# needed for debug toolbar
INTERNAL_IPS = INTERNAL_IPS  # local_settings.py

# CORS HEADERS
CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS
CORS_ALLOW_ALL_ORIGINS = DEBUG  # Allows from all origins when DEBUG mode is on

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
PLUGIN_APPS = [
    'werkzeug_debugger_runserver',
   
 
]

PROJECT_APPS = [
    'appointment.apps.AppointmentConfig',
    'hospital.apps.HospitalConfig',
]

INSTALLED_APPS = DJANGO_APPS + PLUGIN_APPS + PROJECT_APPS


# https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # suppress model warning


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'heartcare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hospital.context_processors.footer_content',
            ],
        },
    },
]

WSGI_APPLICATION = 'heartcare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your password'



STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR  # production, don't forget to run collectstatic
STATICFILES_DIRS = [
    STATICFILES_DIR,
]  # development environment

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# Admin panel configuration ---------------------------------------------------
# https://github.com/farridav/django-jazzmin
# https://django-jazzmin.readthedocs.io/
# JAZZMIN_SETTINGS = CONFIG

ADMIN_URL = 'manage'  # do not include any leading/trailing slashes

# Logging ---------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/topics/logging/

if os.getenv('DISABLE_LOGGING', False):  # for celery in jenkins ci only
    LOGGING_CONFIG = None
LOGGING = LOGGING  # logging.py

# Email -----------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/topics/email/

try:  # optional settings import
    from heartcare.local_settings import EMAIL_BACKEND

    EMAIL_BACKEND = EMAIL_BACKEND
except ImportError:  # use default if not defined in local_settings
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Celery ----------------------------------------------------------------------
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#configuration-and-defaults
CELERY_BROKER_URL = os.getenv(
    'CELERY_BROKER_URL', CELERY_BROKER_URL
)

# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#extensions
CELERY_RESULT_BACKEND = os.getenv(
    'CELERY_RESULT_BACKEND', CELERY_RESULT_BACKEND
)
CELERY_CACHE_BACKEND = os.getenv(
    'CELERY_CACHE_BACKEND', CELERY_CACHE_BACKEND
)

# DbBackup --------------------------------------------------------------------
# https://django-dbbackup.readthedocs.io/

# AWS S3 EXAMPLE
# https://django-dbbackup.readthedocs.io/en/master/storage.html#amazon-s3
# DBBACKUP_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DBBACKUP_STORAGE_OPTIONS = {
#     'access_key': AWS_ACCESS_KEY_ID,
#     'secret_key': AWS_SECRET_ACCESS_KEY,
#     'bucket_name': AWS_STORAGE_BUCKET_NAME,
#     'default_acl': 'private',
#     'location': 'backup/',
# }

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': 'backup/'}


DJANGORESIZED_DEFAULT_SIZE = [300, 300]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True


CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 250,
        'width': 640,
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            [
                'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'
            ],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}
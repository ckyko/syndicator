"""
Django settings for syndicator project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1+zyr@l)0(%jj39miz#(+0(%%9--j1&owhyb2^dht^08rq6-v3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'django_crontab',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'management',
    'django_cron',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'syndicator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'syndicator.wsgi.application'


# databas settings
# try:
#     db_pass = os.environ["DB_PASS"]
# except KeyError:
#     print("Error: environment variable DB_PASS must be set.")
#     exit(1)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'syn',
#         'HOST': 'localhost',
#         'PORT': '',
#         'USER': 'localuser',
#         'PASSWORD': db_pass,
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'simple': {
#             'format': '[%(asctime)s] - %(levelname)s : %(message)s',
#         },
#         'full': {
#             'format': '[%(asctime)s] - %(levelname)s - %(name)s [P%(process)d]: %(message)s',
#         },
#     },
#     'root': {
#         'level': 'DEBUG',
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'django_log': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'tmp/django.log',
#             'formatter': 'full'
#         },
#         'app_log': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'tmp/application.log',
#             'formatter': 'full'
#         },
#         'service_log': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'tmp/service.log',
#             'formatter': 'full'
#         },
#         'audit_log': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'tmp/audit.log',
#             'formatter': 'full'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'django_log'],
#         },
#         'py.warnings': {
#             'handlers': ['console', 'app_log'],
#         },
#         'app': {
#             'handlers': ['console', 'app_log'],
#         },
#         'service': {
#             'handlers': ['service_log'],
#         },
#         'audit': {
#             'handlers': ['audit_log'],
#         },
#     }
# }

# PATH="~/vp35/bin/python"
#
# CRONJOBS = [
#     ('*/1 * * * *', 'management.cron.my_scheduled_job')
# ]

CRON_CLASSES = [
    "management.cron.MyCronJob",
    # ...
]
try:
    EVENTBRITE_TOKEN = os.environ["E_TOKEN"]
except KeyError:
    print("Error: environment variable E_TOKEN must be set.")
    EVENTBRITE_TOKEN = "fake_token"

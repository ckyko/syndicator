
from .base_settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] - %(levelname)s : %(message)s',
        },
        'full': {
            'format': '[%(asctime)s] - %(levelname)s - %(name)s [P%(process)d]: %(message)s',
        },
    },
    'root': {
        'level': 'DEBUG',
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'django_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'tmp/django.log',
            'formatter': 'full'
        },
        'app_log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'tmp/application.log',
            'formatter': 'full'
        },
        'service_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'tmp/service.log',
            'formatter': 'full'
        },
        'audit_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'tmp/audit.log',
            'formatter': 'full'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'django_log'],
        },
        'py.warnings': {
            'handlers': ['console', 'app_log'],
        },
        'app': {
            'handlers': ['console', 'app_log'],
        },
        'service': {
            'handlers': ['service_log'],
        },
        'audit': {
            'handlers': ['audit_log'],
        },
    }
}


# databas settings
# try:
#     db_pass = os.environ["DB_PASS"]
# except KeyError:
#     print("Error: environment variable DB_PASS must be set.")
#     exit(1)
#
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


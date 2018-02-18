from .base_settings import *

DEBUG = False

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
        'level': 'INFO',
    },
    'handlers': {
        'django_log': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'class': 'logging.FileHandler',
            'filename': '/var/log/app/django.log',
            'formatter': 'full'
        },
        'app_log': {
            'level': os.getenv('APP_LOG_LEVEL', 'INFO'),
            'class': 'logging.FileHandler',
            'filename': '/var/log/app/application.log',
            'formatter': 'full'
        },
        'service_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/app/service.log',
            'formatter': 'full'
        },
        'audit_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/app/audit.log',
            'formatter': 'full'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_log'],
        },
        'py.warnings': {
            'handlers': ['app_log'],
        },
        'app': {
            'handlers': ['app_log'],
        },
        'service': {
            'handlers': ['service_log'],
        },
        'audit': {
            'handlers': ['audit_log'],
        },
    }
}

# try:
#     db_host = os.environ["DB_HOST"]
#     db_port = os.environ["DB_PORT"]
#     db_user = os.environ["DB_USER"]
#     db_pass = os.environ["DB_PASS"]
# except KeyError:
#     print("Error: environment variable DB_HOST, DB_PORT, DB_USER, and DB_PASS must be set.")
#     exit(1)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'synprd',
#         'HOST': db_host,
#         'PORT': db_port,
#         'USER': db_user,
#         'PASSWORD': db_pass,
#     }
# }


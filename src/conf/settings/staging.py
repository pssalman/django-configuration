from .base import *

LOCAL_APPS = [
    'storages',
    'anymail',
    'health_check',
    # required
    'health_check.db',
    # stock Django health checkers
    'health_check.cache',
    'health_check.storage',
    # requires celery
    'health_check.contrib.celery',
    # disk and memory utilization; requires psutil
    'health_check.contrib.psutil',
    # requires boto and S3BotoStorage backend
    'health_check.contrib.s3boto_storage',
    'health_check.contrib.rabbitmq',
]  # noqa F405

INSTALLED_APPS += LOCAL_APPS

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'CONN_MAX_AGE': env('DB_CONN_MAX_AGE', cast=int),
        'ATOMIC_REQUESTS': env('DB_ATOMIC_REQUESTS', cast=bool),
    }
}
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

CORS_ALLOW_CREDENTIALS = env('APP_CORS_ALLOW_CREDENTIALS', cast=bool)
CORS_ORIGIN_ALLOW_ALL = env('APP_CORS_ORIGIN_ALLOW_ALL', cast=bool)
# CORS_URLS_REGEX = r'^/api.*$'
# CORS_ORIGIN_WHITELIST = ('*',)
CORS_ORIGIN_WHITELIST = env('APP_CORS_ORIGIN_WHITELIST', cast=Csv(post_process=tuple))

# SECURITY
# ------------------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = env('APP_SECURE_PROXY_SSL_HEADER', cast=Csv(post_process=tuple))
SECURE_SSL_REDIRECT = env("APP_SECURE_SSL_REDIRECT", cast=bool)
SESSION_COOKIE_SECURE = env("APP_SESSION_COOKIE_SECURE", cast=bool)
CSRF_COOKIE_SECURE = env("APP_CSRF_COOKIE_SECURE", cast=bool)
SECURE_HSTS_SECONDS = env('APP_SECURE_HSTS_SECONDS', cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env("APP_SECURE_HSTS_INCLUDE_SUBDOMAINS", cast=bool)
SECURE_HSTS_PRELOAD = env("APP_SECURE_HSTS_PRELOAD", cast=bool)
SECURE_CONTENT_TYPE_NOSNIFF = env("APP_SECURE_CONTENT_TYPE_NOSNIFF", cast=bool)

SESSION_EXPIRE_AT_BROWSER_CLOSE = env("APP_SESSION_EXPIRE_AT_BROWSER_CLOSE", cast=bool)
SESSION_COOKIE_AGE = env('APP_SESSION_COOKIE_AGE', cast=int)
SESSION_SAVE_EVERY_REQUEST = env("APP_SESSION_SAVE_EVERY_REQUEST", cast=bool)
from .base import *

INTERNAL_IPS = [
    '127.0.0.1',
]

LOCAL_APPS = [
    'rosetta',
    'debug_toolbar', 
    'django_extensions'
]

INSTALLED_APPS += LOCAL_APPS

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': os.path.join(RUN_ROOT, 'db.sqlite3'),
        'CONN_MAX_AGE': env('DB_CONN_MAX_AGE', cast=int),      
    }
}

CORS_ALLOW_CREDENTIALS = env('APP_CORS_ALLOW_CREDENTIALS', cast=bool)
CORS_ORIGIN_ALLOW_ALL = env('APP_CORS_ORIGIN_ALLOW_ALL', cast=bool)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

ROSETTA_SHOW_AT_ADMIN_PANEL = True
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
YANDEX_TRANSLATE_KEY = env('APP_YANDEX_TRANSLATE_KEY')
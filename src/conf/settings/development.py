from .base import *

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': os.path.join(RUN_ROOT, 'db.sqlite3'),
        'CONN_MAX_AGE': env('DB_CONN_MAX_AGE', cast=int),      
    }
}
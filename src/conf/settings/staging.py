from .base import *

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
        'ATOMIC_REQUESTS': env('DB_ATOMIC_REQUESTS'),
    }
}
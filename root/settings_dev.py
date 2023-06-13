from root.settings import *  # noqa

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'falcon',
        'USER': 'postgres',
        'PASSWORD': 1,
        'HOST': 'localhost',
        'PORT': 5432
    }
}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "falcon"
    }
}

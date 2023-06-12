from root.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'falcon',
        'USER': 'falcon_user',
        'PASSWORD': 'SsU1Q9nHU0lYoftYOLljPGbSrktFvFXl',
        'HOST': 'dpg-ci3bbgrhp8u1a1eud46g-a.oregon-postgres.render.com',
        'PORT': 5432
    }
}

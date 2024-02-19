from . base import * 


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


REDIS_HOST = 'localhost'
REDIS_HOST = 'redis'
REDIS_PORT = '6379'
REDIS_DB = 1

# Celery Configuration docker
# CELERY_BROKER_URL = os.environ['CELERY_RESULT_BACKEND']
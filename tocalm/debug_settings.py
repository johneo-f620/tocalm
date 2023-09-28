from .settings import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
SECRET_KEY = 'django-insecure-^8xyvs+imzg*hdr*4co^9q$o4bh8!zs)wk8d_cv$d+8#()y))9'
DEBUG = True
DATABASES['default']['NAME'] = BASE_DIR / 'db.sqlite3'

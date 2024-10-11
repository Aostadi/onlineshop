SECRET_KEY = 'django-insecure-)$l^wly)4)!jrq5krk+2pkb=1gn9jqp0f#1g#tr5gp^f!_rv*$'
DEBUG = False

ALLOWED_HOSTS = ['*']
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
    }
}

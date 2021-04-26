import json
from pathlib import Path
from sportswatch.settings import *

from corsheaders.defaults import default_headers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

with open('/etc/sportswatch-api-test-crdentials.json') as json_file:
    credentials = json.load(json_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = credentials.get('SECRET_KEY')
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['test.sportswatchapp.dk', 'www.test.sportswatchapp.dk']

# Application definition
ROOT_URLCONF = 'sportswatch.urls'
WSGI_APPLICATION = 'sportswatch.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': credentials.get('DATABASE_NAME'),
        'USER': credentials.get('DATABASE_USER'),
        'PASSWORD': credentials.get('DATABASE_PASSWORD'),
        'HOST': credentials.get('DATABASE_HOST'),
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'da-DK'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = 'static/'
AUTH_USER_MODEL = 'app.User'

CORS_ALLOWED_ORIGINS = [
    "https://test.sportswatchapp.dk",
    "https://sportswatchapp.dk",
    "https://api.sportswatchapp.dk",
    "https://www.test.sportswatchapp.dk",
    "http://localhost:3000"
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'Content-Language',
]

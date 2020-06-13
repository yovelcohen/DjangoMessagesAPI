import os

import django_heroku
import dotenv

from .config.Consts import STATIC, EN, UTC, SECRET_KEY, DATE_TIME_FORMAT, DATETIME_FORMAT
from .config.DataBase import POSTGRESQL_CONNECTION
from .config.Roots import AppRoots, ALLOWED_HOSTS
from .config.apps.Apps import DjangoApps
from .config.apps.InstalledApps import INSTALLED_APPS
from .config.apps.Middleware import MIDDLEWARE
from .config.auth.PasswordValidators import AUTH_PASSWORD_VALIDATORS
from .config.auth.RestFrameworkAuth import RestFrameworkAuth, \
    REST_DEFAULT_PERMISSIONS_CLASSES, REST_DEFAULT_AUTHENTICATION_CLASSES
from .config.templates.TemplateSettings import TemplateSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.environ[SECRET_KEY]

DEBUG = False

ALLOWED_HOSTS = ALLOWED_HOSTS

INSTALLED_APPS = INSTALLED_APPS.BASE_INSTALLED_APPS
SITE_ID = 1
EMAIL_BACKEND = DjangoApps.EMAIL_BACKEND

AUTH_USER_MODEL = RestFrameworkAuth.AUTH_USER_MODEL

MIDDLEWARE = MIDDLEWARE.BASE_MIDDLEWARE

ROOT_URLCONF = AppRoots.URLS

TEMPLATES = TemplateSettings.TEMPLATES

WSGI_APPLICATION = AppRoots.WSGI
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATABASES = {
    # Local DB
    'default': {
        'ENGINE': POSTGRESQL_CONNECTION['engine'],
        'NAME': POSTGRESQL_CONNECTION['database'],
        'user': POSTGRESQL_CONNECTION['user'],
        'PASSWORD': POSTGRESQL_CONNECTION['password'],
        'HOST': POSTGRESQL_CONNECTION["host"],
    }
}

AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS

LANGUAGE_CODE = EN

TIME_ZONE = UTC

USE_I18N = True

USE_L10N = True

USE_TZ = True

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = f'/{STATIC}/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC)

REST_FRAMEWORK = {
    RestFrameworkAuth.REST_DEFAULT_PERMISSIONS: REST_DEFAULT_PERMISSIONS_CLASSES,
    RestFrameworkAuth.REST_DEFAULT_AUTHENTICATION: REST_DEFAULT_AUTHENTICATION_CLASSES,
    # DATETIME_FORMAT: [DATE_TIME_FORMAT, ]
}
django_heroku.settings(locals())

import os

import django_heroku
import dotenv

from .settings.Consts import STATIC, EN, UTC, SECRET_KEY
from .settings.DataBase import POSTGRESQL_CONNECTION
from .settings.Roots import AppRoots, ALLOWED_HOSTS
from .settings.apps.Apps import DjangoApps
from .settings.apps.InstalledApps import INSTALLED_APPS
from .settings.apps.Middleware import MIDDLEWARE
from .settings.auth.PasswordValidators import AUTH_PASSWORD_VALIDATORS
from .settings.auth.RestFrameworkAuth import RestFrameworkAuth, \
    REST_DEFAULT_PERMISSIONS_CLASSES, REST_DEFAULT_AUTHENTICATION_CLASSES
from .settings.logging.Logging import LOGGING
from .settings.templates.TemplateSettings import TemplateSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env_file = os.path.join(BASE_DIR, ".env")

if os.path.isfile(env_file):
    dotenv.load_dotenv(env_file)

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
CONN_MAX_AGE = 10
REST_FRAMEWORK = {
    RestFrameworkAuth.REST_DEFAULT_PERMISSIONS: REST_DEFAULT_PERMISSIONS_CLASSES,
    RestFrameworkAuth.REST_DEFAULT_AUTHENTICATION: REST_DEFAULT_AUTHENTICATION_CLASSES,
}
LOGGING = LOGGING
django_heroku.settings(locals())

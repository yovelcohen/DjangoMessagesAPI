import os

import django_heroku
import dotenv

from .Settings.Consts import STATIC, EN, UTC, SECRET_KEY
from .Settings.apps.apps import DjangoApps
from .Settings.apps.installed_apps import INSTALLED_APPS
from .Settings.apps.middleware import MIDDLEWARE
from .Settings.auth.password_validators import AUTH_PASSWORD_VALIDATORS
from .Settings.auth.rest_framework_auth import RestFrameworkAuth, \
    REST_DEFAULT_PERMISSIONS_CLASSES, REST_DEFAULT_AUTHENTICATION_CLASSES
from .Settings.database import POSTGRESQL_CONNECTION
from .Settings.roots import AppRoots
from .Settings.templates.templates_settings import TemplateSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.environ[SECRET_KEY]

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = INSTALLED_APPS.BASE_INSTALLED_APPS
SITE_ID = 1
EMAIL_BACKEND = DjangoApps.EMAIL_BACKEND

AUTH_USER_MODEL = RestFrameworkAuth.AUTH_USER_MODEL

MIDDLEWARE = MIDDLEWARE.BASE_MIDDLEWARE

ROOT_URLCONF = AppRoots.URLS

TEMPLATES = TemplateSettings.TEMPLATES

WSGI_APPLICATION = AppRoots.WSGI

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
}

django_heroku.settings(locals())

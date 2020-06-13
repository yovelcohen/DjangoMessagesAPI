class INSTALLED_APPS:
    BASE_INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'rest_framework.authtoken',
        'django.contrib.sites',
        'rest_auth',
        'django_filters',
        'allauth',
        'allauth.account',
        'rest_auth.registration',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.facebook',
        'allauth.socialaccount.providers.twitter',
        'api',
        'drf_yasg'
    ]
    TEST_INSTALLED_APPS = None
    PRODUCTION_INSTALLED_APPS = None

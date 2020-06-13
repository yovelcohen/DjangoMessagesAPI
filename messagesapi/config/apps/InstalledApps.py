class INSTALLED_APPS:
    BASE_INSTALLED_APPS = [
        # Djagno
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        # Rest Framework
        'rest_framework',
        # Auth
        'rest_framework.authtoken',
        'rest_auth',
        'allauth',
        'allauth.account',
        'rest_auth.registration',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.facebook',
        'allauth.socialaccount.providers.twitter',
        # Filters
        'django_filters',
        # API App
        'api',
        # Docs
        'drf_yasg'
    ]
    TEST_INSTALLED_APPS = None
    PRODUCTION_INSTALLED_APPS = None

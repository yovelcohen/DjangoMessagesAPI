REST_DEFAULT_PERMISSIONS_CLASSES = ('rest_framework.permissions.IsAuthenticated',)
REST_DEFAULT_AUTHENTICATION_CLASSES = ('rest_framework.authentication.TokenAuthentication',)


class RestFrameworkAuth:
    REST_DEFAULT_PERMISSIONS = 'DEFAULT_PERMISSION_CLASSES'
    REST_DEFAULT_AUTHENTICATION = 'REST_DEFAULT_AUTHENTICATION'
    AUTH_USER_MODEL = 'api.User'

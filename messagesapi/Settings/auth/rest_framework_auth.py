import datetime

REST_DEFAULT_PERMISSIONS_CLASSES = ('rest_framework.permissions.IsAuthenticated',)
REST_DEFAULT_AUTHENTICATION_CLASSES = ('rest_framework_simplejwt.authentication.JWTAuthentication',)


class RestFrameworkAuth:
    REST_DEFAULT_PERMISSIONS = 'DEFAULT_PERMISSION_CLASSES'
    REST_DEFAULT_AUTHENTICATION = 'REST_DEFAULT_AUTHENTICATION'
    AUTH_USER_MODEL = 'api.User'


JWT_AUTH = {
    # If the secret is wrong, it will raise a jwt.DecodeError.
    'JWT_VERIFY': True,
    'JWT_ALGORITHM': 'HS256',
    # If set to False, JWTs will last forever meaning a leaked token could be used by an attacker.
    'JWT_VERIFY_EXPIRATION': True,

    # Default is datetime.timedelta(seconds=300)(5 minutes).
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),

    'JWT_ALLOW_REFRESH': True,
    'JWT_AUTH_HEADER_PREFIX': '',
}

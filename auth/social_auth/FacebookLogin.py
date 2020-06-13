from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from django.urls import path
from rest_auth.registration.views import SocialLoginView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter



from django.urls import path

from .facebook_login import FacebookLogin
from .twitter_login import TwitterLogin

urlpatterns = [
    path('facebook', FacebookLogin.as_view(), name='fb_login'),
    path('twitter', TwitterLogin.as_view(), name='twitter_login')
]

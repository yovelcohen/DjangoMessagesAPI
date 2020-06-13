from django.urls import path

from .FacebookLogin import FacebookLogin
from .TwitterLogin import TwitterLogin

urlpatterns = [
    path('facebook', FacebookLogin.as_view(), name='fb_login'),
    path('twitter', TwitterLogin.as_view(), name='twitter_login')
]

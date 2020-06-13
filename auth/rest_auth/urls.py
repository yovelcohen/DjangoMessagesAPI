from django.conf.urls import url
from django.urls import include, path
from rest_auth.views import (LoginView, LogoutView, PasswordChangeView,
                             UserDetailsView)

urlpatterns = [
    path('api/sign-up/', include('rest_auth.registration.urls')),
    url(r'^api/login/$', LoginView.as_view(), name='rest_login'),
    url(r'^api/logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^api/user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^api/password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
]

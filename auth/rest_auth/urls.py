from django.conf.urls import url
from django.urls import include, path
from rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordChangeView

urlpatterns = [
    path('api/auth/sign-up/', include('rest_auth.registration.urls')),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
]

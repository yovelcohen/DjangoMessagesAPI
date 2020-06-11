from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/sign-up/', include('rest_auth.registration.urls')),
    path('social/', include('auth.social_auth.urls')),
    path('', include('docs.urls')),
]

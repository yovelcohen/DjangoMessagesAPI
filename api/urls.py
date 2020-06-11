from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
    url('', include(router.urls)),
]

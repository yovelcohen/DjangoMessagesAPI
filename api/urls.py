from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
    url('', include(router.urls)),
]

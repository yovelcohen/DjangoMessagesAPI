from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, MessagesViewSet

users_router = DefaultRouter()
users_router.register(r'users', UserViewSet, basename='users')

messages_router = DefaultRouter()
messages_router.register(r'messages', MessagesViewSet, basename='messages')

urlpatterns = [
    url('', include(users_router.urls)),
    url('', include(messages_router.urls))
]

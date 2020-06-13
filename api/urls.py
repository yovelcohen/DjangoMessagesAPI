from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views.messages_views import MessagesViewSet
from .views.user_views import UserViewSet

messages_router = DefaultRouter()
messages_router.register(r'messages', MessagesViewSet, basename='messages')
user_router = DefaultRouter()
user_router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    url('', include(messages_router.urls)),
    url('', include(user_router.urls))
]

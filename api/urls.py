from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views.MessageView import MessagesViewSet
from .views.UserViews import UserViewSet

messages_router = DefaultRouter()
messages_router.register(r'messages', MessagesViewSet, basename='messages')
user_router = DefaultRouter()
user_router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    url('', include(messages_router.urls)),
    url('', include(user_router.urls))
]

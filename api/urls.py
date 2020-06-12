from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import MessagesViewSet

messages_router = DefaultRouter()
messages_router.register(r'messages', MessagesViewSet, basename='messages')

urlpatterns = [
    url('', include(messages_router.urls))
]

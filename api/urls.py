from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import MessagesViewSet, CreateUserView

messages_router = DefaultRouter()
messages_router.register(r'messages', MessagesViewSet, basename='messages')

urlpatterns = [
    url('users/', CreateUserView.as_view(), name='account-create'),
    url('', include(messages_router.urls))
]

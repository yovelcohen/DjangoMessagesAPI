from django.http import Http404
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from ..models import Message
from ..serializers.MessageSerializers import MessageSerializer
from ..utils.Consts import MessageFields, FILTERS
from ..utils.ViewsConsts import DocsDescriptions, METHODS


@method_decorator(name=METHODS.LIST, decorator=swagger_auto_schema(
    operation_summary=DocsDescriptions.LIST_MESSAGES
))
@method_decorator(name=METHODS.UPDATE, decorator=swagger_auto_schema(
    operation_summary=DocsDescriptions.UPDATE_MESSAGE
))
@method_decorator(name=METHODS.DELETE, decorator=swagger_auto_schema(
    operation_summary=DocsDescriptions.DELETE_MESSAGE
))
class MessagesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing the messages
    associated with the user.
    """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = FILTERS.FILTER_SET
    search_fields = FILTERS.SEARCH_FIELDS
    ordering_fields = FILTERS.ORDERING_FIELDS
    ordering = [MessageFields.DATE, ]

    def get_user(self):
        user = self.request.user
        return user

    def get_queryset(self):
        return Message.objects.filter(sent_to=self.get_user())

    def perform_create(self, serializer):
        """
        Set the sender to the logged in user.
        """
        serializer.save(sender=self.get_user())

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(method=METHODS.GET, operation_description=DocsDescriptions.UNREAD_MESSAGES,
                         operation_summary=DocsDescriptions.UNREAD_MESSAGES_DESCRIPTION)
    @action(detail=True, )
    def unread_messages(self, request, pk):
        """
        Return all of the user's unread messages and it's count.
        """
        queryset = self.get_queryset().filter(mark_read=False)
        count = queryset.count()
        data = self.filter_queryset(queryset)
        serialized_data = MessageSerializer(data, many=True)
        return Response((serialized_data.data, count), status=HTTP_200_OK)

    @swagger_auto_schema(method=METHODS.GET, operation_description=DocsDescriptions.SENT_MESSAGES,
                         operation_summary=DocsDescriptions.SENT_MESSAGES_DESCRIPTION)
    @action(detail=True)
    def sent_messages(self, request, pk):
        """
        Return all messages sent by the user.
        """
        queryset = Message.objects.filter(sender=self.get_user())
        serialized_data = MessageSerializer(queryset, many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)

    @swagger_auto_schema(method=METHODS.GET, operation_description=DocsDescriptions.LAST_50_MESSAGES,
                         operation_summary=DocsDescriptions.LAST_50_MESSAGES_DESCRIPTION)
    @action(detail=True)
    def last_50_messages(self, request, pk):
        """
        Return the user's 50 last messages
        """
        serialized_data = MessageSerializer(self.get_queryset(), many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)

    @swagger_auto_schema(method=METHODS.GET, operation_description=DocsDescriptions.NEWEST_MESSAGE,
                         operation_summary=DocsDescriptions.NEWEST_MESSAGE_DESCRIPTION)
    @action(detail=False)
    def newest_msg(self, request):
        """
        Return the latest message the user received.
        """
        data = self.get_queryset().order_by(f'-{MessageFields.ID}')[0]
        serialized_data = MessageSerializer(data, many=False)
        return Response(serialized_data.data, status=HTTP_200_OK)

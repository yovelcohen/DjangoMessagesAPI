from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from .Serializers.message_serializer import MessageSerializer
from .Utils.Consts import MessageFields, FILTERS
from .models import Message


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
        serializer.save(sender=self.get_user())

    @action(detail=True, )
    def unread_messages(self, request, pk):
        """
        Return all of the user's unread messages.
        """
        data = self.filter_queryset(self.get_queryset())
        serialized_data = MessageSerializer(data, many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)

    @action(detail=True)
    def sent_messages(self, request, pk):
        """
        Return all messages sent by the user.
        """
        queryset = Message.objects.filter(sender=self.get_user())
        serialized_data = MessageSerializer(queryset, many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)

    @action(detail=True)
    def last_50_messages(self, request, pk):
        """
        Return the user's 50 last messages
        """
        serialized_data = MessageSerializer(self.get_queryset(), many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)

    @action(detail=False)
    def newest_msg(self, request):
        """
        Return the latest message the user received.
        """
        data = self.get_queryset().order_by(f'-{MessageFields.ID}')[0]
        serialized_data = MessageSerializer(data, many=False)
        return Response(serialized_data.data, status=HTTP_200_OK)

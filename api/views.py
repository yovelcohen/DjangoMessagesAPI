from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .Serializers.message_serializer import MessageSerializer
from .Serializers.user_serializer import UserSerializer
from .Utils.Consts import MessageFields
from .models import Message


class MessagesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing the messages
    associated with the user.
    """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [MessageFields.MARK_READ]

    def get_user(self):
        user = self.request.user
        return user

    def get_queryset(self):
        return Message.objects.filter(sent_to=self.get_user())

    @action(detail=True)
    def sent_messages(self):
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
        queryset = Message.objects.filter(sent_to=self.get_user())
        serialized_data = MessageSerializer(queryset, many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)

    @action(detail=True, )
    def unread_messages(self, request, pk):
        """
        Return all of the user's unread messages.
        """
        data = self.filter_queryset(self.get_queryset())
        serialized_data = MessageSerializer(data, many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)


class CreateUserView(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

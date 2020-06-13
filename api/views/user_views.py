from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import User
from ..serializers.user_serializers import UserSerializer
from ..utils.views_consts import DocsDescriptions


class UserViewSet(GenericViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    @swagger_auto_schema(operation_summary=DocsDescriptions.LIST_USERS)
    def list(self, request):
        serializer = UserSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary=DocsDescriptions.RETRIEVE_USER)
    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

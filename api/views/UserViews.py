from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ..serializers.UserSerializers import UserSerializer
from ..utils.ViewsConsts import DocsDescriptions
from ..models import User


class UserViewSet(ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary=DocsDescriptions.LIST_USERS)
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary=DocsDescriptions.RETRIEVE_USER)
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

from api.models import User
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from api.Utils.Consts import UserFields, SerializerFields


class UserSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedRelatedField(view_name='UserViewSet', read_only=True)

    class Meta:
        model = User
        fields = (
            UserFields.URL, UserFields.EMAIL, UserFields.USER_NAME,
            UserFields.FIRST_NAME, UserFields.LAST_NAME,
            UserFields.PASSWORD
        )
        extra_kwargs = {UserFields.PASSWORD: {SerializerFields.WRITE_ONLY: True}, }

    def create(self, validated_data):
        password = validated_data.pop(UserFields.PASSWORD)
        user = User(**validated_data)
        # Hash passwords
        user.set_password(password)
        # Create new messages
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.UserFields.EMAIL = validated_data.get(UserFields.EMAIL, instance.UserFields.EMAIL)
        instance.save()
        return instance

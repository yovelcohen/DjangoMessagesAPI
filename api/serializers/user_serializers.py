from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models import User
from ..utils.consts import UserFields


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=32,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data[UserFields.USER_NAME], validated_data[UserFields.EMAIL],
                                        validated_data[UserFields.PASSWORD])
        return user

    class Meta:
        model = User
        fields = (UserFields.ID, UserFields.USER_NAME, UserFields.EMAIL, UserFields.PASSWORD)

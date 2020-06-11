from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    messages = StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        # Hash passwords
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance

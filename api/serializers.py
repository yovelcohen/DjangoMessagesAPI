from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField

from .models import User, Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('subject', 'sent_to', 'content')


class UserSerializer(HyperlinkedModelSerializer):
    messages = MessageSerializer(many=True)
    url = HyperlinkedRelatedField(view_name='UserViewSet', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'messages')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        # Hash passwords
        user.set_password(password)
        msg_data = validated_data.pop('messages')
        User.objects.create(**validated_data)
        for msg_data in msg_data:
            Message.objects.create(user=user, **msg_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance

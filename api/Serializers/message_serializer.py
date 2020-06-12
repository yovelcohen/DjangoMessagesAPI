from api.Utils.Consts import MessageFields
from api.models import Message
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class MessageSerializer(ModelSerializer):
    mark_read = serializers.BooleanField(default=False)

    class Meta:
        model = Message
        fields = (MessageFields.ID, MessageFields.SENDER, MessageFields.SUBJECT,
                  MessageFields.SENT_TO, MessageFields.CONTENT, MessageFields.MARK_READ)
        read_only_fields = (MessageFields.DATE,)

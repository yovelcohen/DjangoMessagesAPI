from ..utils.Consts import MessageFields
from ..models import Message
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class MessageSerializer(ModelSerializer):
    mark_read = serializers.BooleanField(default=False)
    sent_at = serializers.DateTimeField()
    class Meta:
        model = Message
        fields = (MessageFields.ID, MessageFields.SENDER, MessageFields.SUBJECT,
                  MessageFields.SENT_TO, MessageFields.CONTENT, MessageFields.DATE, MessageFields.MARK_READ)
        read_only_fields = (MessageFields.DATE, MessageFields.SENDER, MessageFields.ID)

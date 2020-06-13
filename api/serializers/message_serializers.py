from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ..models import Message
from ..utils.consts import DATE_TIME_FORMAT, MessageFields


class MessageSerializer(ModelSerializer):
    mark_read = serializers.BooleanField(default=False)
    sent_at = serializers.DateTimeField(format=DATE_TIME_FORMAT, default=timezone.now)

    class Meta:
        model = Message
        fields = (MessageFields.ID, MessageFields.SENDER, MessageFields.SUBJECT,
                  MessageFields.SENT_TO, MessageFields.CONTENT, MessageFields.DATE, MessageFields.MARK_READ)
        read_only_fields = (MessageFields.DATE, MessageFields.SENDER, MessageFields.ID)

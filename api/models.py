from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .Utils.Consts import MessageFields
from .Utils.Validators import validate_message_content


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.DO_NOTHING,
                               )

    sent_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.DO_NOTHING,
                                related_name=MessageFields.SENT_TO)
    sent_at = models.DateTimeField(default=timezone.now)

    subject = models.CharField(max_length=120,
                               help_text='Message subject is limited to 120 characters')

    content = models.TextField(validators=[validate_message_content],
                               help_text="Message Body")
    mark_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} : \n {self.content} "


class User(AbstractUser):
    pass

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError


def validate_message_content(content):
    if content is not None:
        pass
    elif content is None or content == "" or content.isspace():
        raise ValidationError("Body of message can't be empty!")


class Message(models.Model):
    sender = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    sent_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.DO_NOTHING,
                                related_name='sent_to')
    sent_at = models.DateTimeField(default=timezone.now)

    subject = models.CharField(max_length=120,
                               help_text='Message subject is limited to 120 characters')

    content = models.TextField(validators=[validate_message_content],
                               help_text="Message Body")

    def __str__(self):
        return f"{self.subject} : \n {self.content} "


class User(AbstractUser):
    username = models.CharField(blank=True,
                                null=True,
                                max_length=120)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    messages = models.ForeignKey(related_name='messages',
                                 on_delete=models.CASCADE,
                                 to=Message,
                                 null=True
                                 )

    def __str__(self):
        return f"{self.username}"

    def read(self):
        self.last_read_date = timezone.now()
        self.save()

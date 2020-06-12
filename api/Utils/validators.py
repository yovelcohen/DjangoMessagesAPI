from rest_framework.exceptions import ValidationError


def validate_message_content(content):
    if content is not None:
        pass
    elif content is None or content == "" or content.isspace():
        raise ValidationError("Body of message can't be empty!")

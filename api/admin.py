from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from .models import User, Message

admin.site.register(User)
admin.site.register(Message)
TokenAdmin.raw_id_fields = ['user']

from django.contrib import admin

from chat_app.models import Chat, Message

admin.site.register(Message)
admin.site.register(Chat)

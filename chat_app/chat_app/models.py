from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime

User = get_user_model()


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    # chat_id = models.ForeignKey(Chat, on_delete=models.PROTECT)
    registered_time = models.DateTimeField(auto_created=True)
    edited_time = models.DateTimeField(auto_created=True)
    deleted = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.content} - read: {self.is_read} from: {self.sender}'


class Chat(models.Model):
    user_id = models.ForeignKey('UserProfile', on_delete=models.PROTECT)
    participants = models.ManyToManyField('User')
    messages = models.ManyToManyField(Message, blank=True)
    register_date = models.DateTimeField(default=datetime.now, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    close_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.id} - chat: {self.participants}'

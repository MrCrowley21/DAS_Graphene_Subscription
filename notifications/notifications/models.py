from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# in-app notification
class Notifications(models.Model):
    sender = models.ForeignKey(User, null=True, blank=True, related_name='n_sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, null=True, blank=True, related_name='n_receiver', on_delete=models.CASCADE)
    status = models.CharField(max_length=264, null=True, blank=True, default='unread')
    type = models.CharField(max_length=264, null=True, blank=True)



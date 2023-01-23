import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync,sync_to_async
from channels.layers import get_channel_layer
from django.contrib.auth.models import AnonymousUser

from notifications.models import User, Notifications


@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except:
        return AnonymousUser()


@database_sync_to_async
def create_notification(receiver, typeof='notification', status='unread'):
    notification = Notifications.objects.create(n_receiver=receiver, type=typeof)
    return notification.receiver.username, notification.typeof


class NotificationConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        await self.accept()
        await self.send(json.dumps({'type': 'websocket.send', 'text': 'Test notification'}))
        self.room_name = 'test'
        self.room_group_name = 'test_group'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.send({'type': 'websocket.send', 'text': 'room'})

    async def websocket_receive(self, event):
        data_to_get = json.loads(event['text'])
        user_to_get = await get_user(int(data_to_get))
        get_of = await create_notification(user_to_get)
        self.room_group_name = 'test_consumer_group'
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            self.room_group_name,{"type": "send_notification", "value": json.dumps(get_of)})

    async def websocket_disconnect(self, event):
        print('disconnect', event)

    async def send_notification(self, event):
        await self.send(json.dumps({"type": "websocket.send", "data": event}))



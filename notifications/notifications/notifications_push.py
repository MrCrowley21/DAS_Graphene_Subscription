from push_notifications.models import GCMDevice
from fcm_django.models import FCMDevice

from settings import PUSH_NOTIFICATIONS_SETTINGS


def send_notification(user_ids, title, message, data):
    try:
        device_n = FCMDevice.objects.filter(user__in=user_ids).first()
        result = device_n.send_message(title=title, body=message, data=data, sound=True)
        return result
    except:
        pass


# this should be enough for push notifications
device = GCMDevice.objects.get(user='user', registration_id='put here device registration id')
device.send_message("New Notification")

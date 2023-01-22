import graphene
from django.contrib.auth import get_user_model
from django_filters import FilterSet, OrderingFilter
from graphene import relay
from graphene_django import DjangoObjectType

from chat_app.models import Chat, Message


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "last_name", "first_name"]


class ChatFilter(FilterSet):
    class Meta:
        model = Chat
        fields = ("last_modified", "name")
        order_by = ("last_modified", "id")


class ChatType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Chat
        fields = '_all_'
        interfaces = (relay.Node,)


class MessageFilter(FilterSet):
    class Meta:
        model = Message
        fields = ("is_read", "deleted")
        order_by = ("id", "registered_time")


class MessageType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = Message
        fields = '_all_'
        interfaces = (relay.Node,)

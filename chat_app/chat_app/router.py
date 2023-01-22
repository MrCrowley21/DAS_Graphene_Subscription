import channels
from django.core.asgi import get_asgi_application
from django.urls import path
import channels.auth

from chat_app.schema import GraphQLWsConsumer

application = channels.routing.ProtocolTypeRouter({
    "websocket": channels.auth.AuthMiddlewareStack(
        channels.routing.URLRouter([
            path("ws/graphql", GraphQLWsConsumer.as_asgi()),
        ])
    ),
})

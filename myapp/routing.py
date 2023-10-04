# file_viewer/routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from viewer import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/update_file/", consumers.UpdateFileConsumer.as_asgi()),
    ]),
})

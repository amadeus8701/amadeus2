from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws://ec2-52-78-22-235.ap-northeast-2.compute.amazonaws.com:8080/some_path/", consumers.MyConsumer.as_asgi()),
    ]),
})
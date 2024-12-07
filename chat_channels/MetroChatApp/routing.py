from django.urls import path
from .consumers import ChatConsumer
# "urls.py do Django Channels"

# WebSocket responsável por conectar a URL com o consumidor
# OBS: no futuro provavelmente n precisaremos disso (chat de user e IA, somente)
websocket_urlpatterns = [
    path('ws/notification/<str:room_name>/', ChatConsumer.as_asgi()),
]
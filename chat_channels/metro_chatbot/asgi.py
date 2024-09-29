"""
ASGI config for metro_chatbot project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from MetroChatApp import routing

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metro_chatbot.settings')

django_asgi_app = get_asgi_application()

# Mapeando a URL do WebSocket criada em routing
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    )
})

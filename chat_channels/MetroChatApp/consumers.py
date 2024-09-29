import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from MetroChatApp.models import *
# Associado ao Django Channels -/ consumidores de WebSocket
# Parecido com views, mas com WebSockets, protocolos HTTP de longa duração

class ChatConsumer(AsyncWebsocketConsumer):
    # front conecta com esse socket (consumidor)
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.accept()
    # Desconecta "cliente"
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    # Método receive (GET do javascript Form botão 'submit')
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json

        event = {
            'type': 'send_message', #Nome do método chamado
            'message': message,
        }

        # Para cada usuário existente na room mandamos a função de enviar msg
        # OBS: no futuro provavelmente n precisaremos disso (chat de user e IA, somente)
        await self.channel_layer.group_send(self.room_name, event)

    async def send_message(self, event):
        # Recebe a msg e data_json
        data = event['message']
        # Cria a mensagem baseada nos dados recebidos do front(js)
        await self.create_message(data=data)
        # Cria dic e manda para todos os usuário conectados na room
        # OBS: no futuro provavelmente n precisaremos disso (chat de user e IA, somente)
        response_data = {
            'sender': data['sender'],
            'message': data['message']
        }
        await self.send(text_data=json.dumps({'message': response_data}))
    
    # "Falando" para o django que estamos praticando manipulação de dados 
    @database_sync_to_async
    def create_message(self, data):
        # Pega o objeto room_name do front(js)
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        # Verifica se a msg ja foi salva no database, para prevenir usuários simultâneos de salvar a mesma msg
        # OBS: no futuro provavelmente n precisaremos disso (chat de user e IA, somente)
        if not Message.objects.filter(message=data['message']).exists():
            new_message = Message(room=get_room_by_name, sender=data['sender'], message=data['message'])
            new_message.save()
    

import json
from MetroChatApp.ia_scripts.llm import simula_resposta_ia
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
        # Lógica por tempo (2 horas) inserir aqui possivelmente
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    # Método receive (GET do javascript Form botão 'submit')
    # Processa a 'message' e ativa resposta da IA
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        
        # Simulador de resposta de IA
        resposta_ia = simula_resposta_ia(message)

        # Enviar mensagem do usuário no front
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': 'user'
        }))

        # Enviar resposta da IA
        await self.send(text_data=json.dumps({
            'message': {
                'message': resposta_ia,
                'sender': 'IA'
            }
        }))
    
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
    

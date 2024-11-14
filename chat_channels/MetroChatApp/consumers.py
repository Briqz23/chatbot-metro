import json
from MetroChatApp.ia_scripts.llm import obter_resposta_ia
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from MetroChatApp.models import *
# Associado ao Django Channels -/ consumidores de WebSocket
# Parecido com views, mas com WebSockets, protocolos HTTP de longa duração

class ChatConsumer(AsyncWebsocketConsumer):


    # front conecta com esse socket (consumidor)
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        self.disconnected_by_user = False
        self.chat_data = {  # Inicializa cjat_data na conexão
            "room_name": self.room_name.replace("room_", ""),
            "chat_history": []
        }
        await self.accept()
        
    # Desconecta "cliente"
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        if self.disconnected_by_user:
            await self.close_chat()

    # Método receive (GET do javascript Form botão 'submit')
    # Processa a 'message' e ativa resposta da IA
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if 'action' in text_data_json and text_data_json['action'] == 'close':
            self.disconnected_by_user = True
            return
        message_obj = text_data_json
        message_unica = text_data_json['message']
        room_name = text_data_json['room_name']
        sender = text_data_json['sender']        

        # Nova mensagem do usuário no histórico
        self.chat_data["chat_history"].append({"role": "user", "content": message_unica})  
        # print(f"ANTES DE EXECUTAR A FUNÇÃO DA RESPOSTA IA: \n{self.chat_data}")
        # Simulador de resposta de IA
        resposta_ia = obter_resposta_ia(message_unica, self.chat_data)

        # Nova mensagem da IA no histórico
        self.chat_data["chat_history"].append({"role": "AI", "content": resposta_ia})
        # print(f"DEPOIS DE EXECUTAR A FUNÇÃO DA RESPOSTA IA: \n{self.chat_data}")

        # Enviar mensagem do usuário no front
        await self.send(text_data=json.dumps({
            'message': message_obj,
            'sender': 'user'
        }))

        # Enviar resposta da IA
        await self.send(text_data=json.dumps({
            'message': {
                'message': resposta_ia,
                'sender': 'IA'
            }
        }))

        # Armazenando as mensagens no BD
        await self.create_message({
            'message': message_unica,
            'room_name': room_name,
            'sender': sender
        })

        await self.create_message({
            'message': resposta_ia,
            'room_name': room_name,
            'sender': 'IA'
        })

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
        
    @database_sync_to_async
    def close_chat(self):
        try:
            room = Room.objects.get(room_name=self.room_name.replace("room_", ""))
            # Apaga room e messages
            Message.objects.filter(room=room).delete()
            room.delete()

        except Room.DoesNotExist:
            pass
from django.test import TestCase
from django.urls import reverse
from .models import Room, Message

# Testes dos models

class RoomTestCase(TestCase):
    def setUp(self):
        self.room = Room.objects.create(room_name="testroom")

    def test_room_creation(self):
        self.assertEqual(self.room.room_name, "testroom")
    
    def test_room_str(self):
        self.assertEqual(str(self.room), "testroom")

class MessageTestCase(TestCase):
    def setUp(self):
        self.room = Room.objects.create(room_name="room_teste")
        self.message = Message.objects.create(
            room=self.room,
            sender="user_3dfh",
            message="Olá, hoje a linha 5 deu problema?"
        )

    def test_message_content(self):
        self.assertEqual(self.message.message, "Olá, hoje a linha 5 deu problema?")
    
    def test_message_room_relation(self):
        # Relação da mensagem com a sala
        self.assertEqual(self.message.room, self.room)

# Teste geral da API

class StatusMetroApiTestCase(TestCase):
    def test_status_metro_api(self):
        response = self.client.get(reverse('status_metro_api'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)  # resposta = JSON dict
        self.assertIn("linhas", response.json())
        self.assertIn("hora_agora", response.json())


# Testes das views e urls

class MessageViewTestCase(TestCase):
    def setUp(self):
        self.room = Room.objects.create(room_name="room_teste")
        self.username = "user_3dfh"
        self.url = reverse('room', kwargs={"room_name": self.room.room_name, "username": self.username})

    def test_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_message_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'message.html')



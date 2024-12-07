from django.db import models
# Modelos de dados do app, cada modelo vira uma tabela no bd

class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    # Toda msg deve ser atribuída a um objeto room
    # Se uma room for deletada, msgs tb serão deletadas
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return str(self.room)
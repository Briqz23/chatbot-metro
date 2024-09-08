from django.db import models

# Create your models here.
#path chat/models.py
from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    title = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}:{self.title}"

class ChatMessage(models.Model):
    id = models.AutoField(primary_key=True)
    conversation = models.ForeignKey(Conversation, default=None, on_delete=models.CASCADE)
    user_response = models.TextField(null=True, default='')
    ai_response = models.TextField(null=True, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.conversation}: {self.id}"
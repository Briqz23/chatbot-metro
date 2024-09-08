from rest_framework import serializers
from .models import ChatMessage, Conversation

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Conversation
        fields= '__all__'
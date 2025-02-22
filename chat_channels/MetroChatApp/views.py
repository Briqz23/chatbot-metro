from django.shortcuts import redirect, render
from .models import Room, Message
from MetroChatApp.webscraping.api import obter_status_metro
import secrets
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
# Tratam as reqs HTTP e retornam respostas
def CreateRoom(request):
    if request.method == 'POST':
        # Gera usuário e room 
        username = "user_" + secrets.token_hex(2)
        room_name = secrets.token_hex(8)

        # Salva dados na session
        request.session['room_name'] = room_name
        request.session['username'] = username

        new_room, created = Room.objects.get_or_create(room_name=room_name)
        # Retorna para nova room com a função MessageView
        return redirect('room', room_name=new_room.room_name, username=username)
    return render(request, 'index.html')
    

def MessageView(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)

    # Response para o front(js)
    context = {
        "messages": get_messages,
        "user": username,
        "room_name": room_name,
    }
    
    return render(request, 'message.html', context)

def MapaView(request):
    room_name = request.session.get('room_name')
    username = request.session.get('username')

    context = {
        "room_name": room_name,
        "username": username,
    }
    return render(request, 'mapa.html', context)

def StatusView(request):
    room_name = request.session.get('room_name')
    username = request.session.get('username')

    context = {
        "room_name": room_name,
        "username": username,
    }
    return render(request, 'status.html', context)

@cache_page(150)
def status_metro_api(request):
    linhas, hora_agora = obter_status_metro()
    return JsonResponse({"linhas": linhas, "hora_agora": hora_agora})
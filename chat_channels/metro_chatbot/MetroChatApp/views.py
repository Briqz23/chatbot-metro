from django.shortcuts import redirect, render
from .models import Room, Message
# Tratam as reqs HTTP e retornam respostas

def CreateRoom(request):
    if request.method == 'POST':
         
        username = request.POST['username']
        room = request.POST['room']

        # Ver se a room ja existe, se não, cria uma 
        try:
            get_room = Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
        # Retorna para nova room com a função MessageView
        return redirect('room', room_name=room, username=username)
    
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

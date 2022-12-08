from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, redirect

from .models import Room, Message
from .forms import RoomForm


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/rooms/')
    else:
        form = RoomForm()

    context = {
        'form': form
    }

    return render(request, 'room/add_room.html', context)

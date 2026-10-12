"""View-функции приложения помещений."""
from django.shortcuts import render
from models.rooms import find_room_by_id
from storage import load_rooms


def rooms(request):
    """Список помещений."""
    context = {"rooms": load_rooms()}
    return render(request, "rooms/room_list.html", context)


def room_detail(request, room_id):
    """Страница помещения."""
    room = find_room_by_id(load_rooms(), room_id)
    context = {"room": room}
    return render(
        request,
        "rooms/room_detail.html",
        context,
        status=404 if room is None else 200,
    )

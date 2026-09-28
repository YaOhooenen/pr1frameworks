"""Тесты класса Room и функций работы с помещениями."""
from models import Room
from models.rooms import (
    add_room,
    find_room,
    check_room_capacity,
    sort_rooms_by_capacity,
)


def test_room_creation():
    room = Room(1, "Аудитория 301", 30)
    assert room.id == 1
    assert room.name == "Аудитория 301"
    assert room.capacity == 30


def test_room_is_suitable_for():
    room = Room(1, "Аудитория 301", 30)
    assert room.is_suitable_for(20) is True
    assert room.is_suitable_for(40) is False


def test_room_str():
    room = Room(1, "Аудитория 301", 30)
    assert "Аудитория 301" in str(room)
    assert "30" in str(room)


def test_add_room():
    rooms = []
    room = add_room(rooms, "Аудитория 301", 30)
    assert len(rooms) == 1
    assert room is rooms[0]


def test_find_room():
    rooms = []
    add_room(rooms, "Аудитория 301", 30)
    add_room(rooms, "Спортзал", 100)
    result = find_room(rooms, "аудитория")
    assert len(result) == 1
    assert result[0].name == "Аудитория 301"


def test_check_room_capacity():
    rooms = []
    add_room(rooms, "Конференц-зал", 60)
    assert check_room_capacity(rooms, 1, 50) is True
    assert check_room_capacity(rooms, 1, 100) is False


def test_sort_rooms():
    rooms = []
    add_room(rooms, "Большой зал", 100)
    add_room(rooms, "Малый зал", 10)
    sorted_rooms = sort_rooms_by_capacity(rooms)
    assert sorted_rooms[0].name == "Малый зал"
    assert sorted_rooms[1].name == "Большой зал"

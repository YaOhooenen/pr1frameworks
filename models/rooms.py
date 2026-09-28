"""Модель помещения и функции работы с коллекцией помещений."""
from typing import List, Optional


class Room:
    """Помещение, в котором проводится уборка."""

    def __init__(
        self, room_id: int, name: str, capacity: int
    ) -> None:
        """Создать объект помещения."""
        self.id = room_id
        self.name = name
        self.capacity = capacity

    def is_suitable_for(self, people_count: int) -> bool:
        """Проверить, подходит ли помещение по вместимости."""
        return self.capacity >= people_count

    def __str__(self) -> str:
        """Строковое представление помещения."""
        return f"{self.name}, вместимость {self.capacity} чел."

    @staticmethod
    def validate_capacity(capacity: int) -> bool:
        """Проверить корректность вместимости."""
        return capacity > 0


def add_room(
    rooms: List[Room], name: str, capacity: int
) -> Optional[Room]:
    """Создать объект Room и добавить его в коллекцию."""
    if not Room.validate_capacity(capacity):
        return None
    room_id = len(rooms) + 1
    room = Room(room_id, name, capacity)
    rooms.append(room)
    return room


def find_room(
    rooms: List[Room], query: str
) -> List[Room]:
    """Найти помещения по подстроке названия."""
    query_lower = query.lower()
    return [r for r in rooms if query_lower in r.name.lower()]


def find_room_by_id(
    rooms: List[Room], room_id: int
) -> Optional[Room]:
    """Найти помещение по идентификатору."""
    for room in rooms:
        if room.id == room_id:
            return room
    return None


def check_room_capacity(
    rooms: List[Room], room_id: int, min_capacity: int
) -> bool:
    """Проверить вместимость помещения (через метод объекта)."""
    room = find_room_by_id(rooms, room_id)
    if room is None:
        return False
    return room.is_suitable_for(min_capacity)


def filter_rooms_by_capacity(
    rooms: List[Room], min_capacity: int
) -> List[Room]:
    """Отобрать помещения по вместимости."""
    return [r for r in rooms if r.is_suitable_for(min_capacity)]


def sort_rooms_by_capacity(
    rooms: List[Room],
) -> List[Room]:
    """Отсортировать помещения по вместимости."""
    return sorted(rooms, key=lambda r: r.capacity)


def show_rooms(rooms: List[Room]) -> None:
    """Вывести список помещений в виде таблицы."""
    if not rooms:
        print("Список помещений пуст.")
        return
    print(f"\n{'ID':<4}{'Название':<25}{'Вместимость':<15}")
    print("-" * 44)
    for r in rooms:
        print(f"{r.id:<4}{r.name:<25}{r.capacity:<15}")

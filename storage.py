"""Сохранение и загрузка данных."""
import json
import os
from typing import List

from models import Room, User, CleaningTask, Order
from models.rooms import find_room_by_id
from models.users import find_user_by_id
from models.tasks import find_task_by_id


def _load_json(filename: str) -> list:
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Ошибка чтения {filename}: {e}")
        return []


def _save_json(filename: str, data: list) -> None:
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"Ошибка записи {filename}: {e}")


def load_rooms(filename: str = "data/rooms.json") -> List[Room]:
    return [
        Room(item["id"], item["name"], item["capacity"])
        for item in _load_json(filename)
    ]


def save_rooms(
    rooms: List[Room], filename: str = "data/rooms.json"
) -> None:
    data = [
        {"id": r.id, "name": r.name, "capacity": r.capacity}
        for r in rooms
    ]
    _save_json(filename, data)


def load_users(filename: str = "data/users.json") -> List[User]:
    return [User.from_data(item) for item in _load_json(filename)]


def save_users(
    users: List[User], filename: str = "data/users.json"
) -> None:
    data = [
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ]
    _save_json(filename, data)


def load_tasks(
    rooms: List[Room],
    filename: str = "data/tasks.json",
) -> List[CleaningTask]:
    data = _load_json(filename)
    tasks = []
    for item in data:
        room = find_room_by_id(rooms, item["room_id"])
        if room is None:
            continue
        task = CleaningTask(
            item["id"], room, item["task_date"],
            item.get("description", ""),
        )
        task.is_cancelled = item.get("is_cancelled", False)
        tasks.append(task)
    return tasks


def save_tasks(
    tasks: List[CleaningTask],
    filename: str = "data/tasks.json",
) -> None:
    data = [
        {
            "id": t.id,
            "room_id": t.room.id,
            "task_date": t.task_date,
            "description": t.description,
            "is_cancelled": t.is_cancelled,
        }
        for t in tasks
    ]
    _save_json(filename, data)


def load_orders(
    users: List[User],
    tasks: List[CleaningTask],
    filename: str = "data/orders.json",
) -> List[Order]:
    """Загрузить заказы, восстановив связи с User и CleaningTask."""
    data = _load_json(filename)
    orders = []
    for item in data:
        user = find_user_by_id(users, item["user_id"])
        task = find_task_by_id(tasks, item["task_id"])
        if user is None or task is None:
            print(
                f"Пропущен заказ {item['id']}: "
                f"не найден пользователь или задача"
            )
            continue
        order = Order(
            item["id"], user, task, item["order_date"],
        )
        order.is_cancelled = item.get("is_cancelled", False)
        orders.append(order)
    return orders


def save_orders(
    orders: List[Order],
    filename: str = "data/orders.json",
) -> None:
    """Сохранить заказы в JSON (хранятся ID связей)."""
    data = [
        {
            "id": o.id,
            "user_id": o.user.id,
            "task_id": o.task.id,
            "order_date": o.order_date,
            "is_cancelled": o.is_cancelled,
        }
        for o in orders
    ]
    _save_json(filename, data)

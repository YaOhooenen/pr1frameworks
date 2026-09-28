"""Сохранение и загрузка данных с преобразованием в объекты."""
import json
import os
from typing import List

from models import Room, User, CleaningTask, Schedule
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


# --- Rooms ---
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


# --- Users ---
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


# --- Tasks ---
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


# --- Schedule ---
def load_schedules(
    schedules_rooms: List[Room],
    users: List[User],
    tasks: List[CleaningTask],
    filename: str = "data/schedule.json",
) -> List[Schedule]:
    """Загрузить расписание, восстановив связи с Room/User/Task."""
    data = _load_json(filename)
    schedules = []
    for item in data:
        room = find_room_by_id(schedules_rooms, item["room_id"])
        user = find_user_by_id(users, item["user_id"])
        task = find_task_by_id(tasks, item["task_id"])
        if room is None or user is None or task is None:
            print(f"Пропущена запись {item['id']}: связи не найдены")
            continue
        s = Schedule(
            item["id"], task, room, user,
            item["scheduled_date"],
        )
        schedules.append(s)
    return schedules


def save_schedules(
    schedules: List[Schedule],
    filename: str = "data/schedule.json",
) -> None:
    data = [
        {
            "id": s.id,
            "task_id": s.task.id,
            "room_id": s.room.id,
            "user_id": s.user.id,
            "scheduled_date": s.scheduled_date,
        }
        for s in schedules
    ]
    _save_json(filename, data)

"""Тесты класса CleaningTask и функций работы с задачами."""
from models import Room, CleaningTask
from models.tasks import (
    is_room_available,
    create_task,
    cancel_task,
)


def test_task_creation():
    room = Room(1, "Аудитория 301", 30)
    task = CleaningTask(1, room, "2026-09-15", "влажная уборка")
    assert task.id == 1
    assert task.room is room
    assert task.task_date == "2026-09-15"
    assert task.description == "влажная уборка"
    assert task.is_cancelled is False


def test_task_cancel():
    room = Room(1, "Аудитория 301", 30)
    task = CleaningTask(1, room, "2026-09-15")
    task.cancel()
    assert task.is_cancelled is True


def test_task_str():
    room = Room(1, "Аудитория 301", 30)
    task = CleaningTask(1, room, "2026-09-15")
    text = str(task)
    assert "Аудитория 301" in text
    assert "2026-09-15" in text


def test_duplicate_task_forbidden():
    room = Room(1, "Аудитория 301", 30)
    tasks = []
    create_task(tasks, room, "2026-09-15", "уборка")
    assert is_room_available(tasks, room, "2026-09-15") is False


def test_cancelled_task_does_not_block():
    room = Room(1, "Аудитория 301", 30)
    tasks = []
    task = create_task(tasks, room, "2026-09-15", "уборка")
    cancel_task(tasks, task.id)
    assert is_room_available(tasks, room, "2026-09-15") is True

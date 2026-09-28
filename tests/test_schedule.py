"""Тесты класса Schedule."""
from models import Room, User, CleaningTask, Schedule
from models.schedule import (
    add_schedule, find_schedules_by_user, find_schedules_by_room,
)


def test_schedule_creation():
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван", "iv@e.ru")
    task = CleaningTask(1, room, "2026-09-15", "влажная уборка")
    s = Schedule(1, task, room, user, "2026-09-15")
    assert s.task is task
    assert s.room is room
    assert s.user is user


def test_add_schedule():
    schedules = []
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван", "iv@e.ru")
    task = CleaningTask(1, room, "2026-09-15")
    s = add_schedule(schedules, task, room, user, "2026-09-15")
    assert len(schedules) == 1
    assert s is schedules[0]


def test_find_by_user():
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван", "iv@e.ru")
    task = CleaningTask(1, room, "2026-09-15")
    schedules = []
    add_schedule(schedules, task, room, user, "2026-09-15")
    assert len(find_schedules_by_user(schedules, 1)) == 1
    assert len(find_schedules_by_user(schedules, 2)) == 0


def test_find_by_room():
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван", "iv@e.ru")
    task = CleaningTask(1, room, "2026-09-15")
    schedules = []
    add_schedule(schedules, task, room, user, "2026-09-15")
    assert len(find_schedules_by_room(schedules, 1)) == 1
    assert len(find_schedules_by_room(schedules, 2)) == 0

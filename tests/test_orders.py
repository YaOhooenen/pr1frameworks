"""Тесты класса Order."""
from models import Room, User, CleaningTask, Order
from models.orders import (
    create_order,
    find_orders_by_user, find_orders_by_room,
)


def test_order_creation():
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван", "iv@e.ru")
    task = CleaningTask(1, room, "2026-09-15", "уборка")
    order = Order(1, user, task, "2026-09-10")
    assert order.user is user
    assert order.task is task
    assert order.is_cancelled is False


def test_order_cancel():
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван", "iv@e.ru")
    task = CleaningTask(1, room, "2026-09-15")
    order = Order(1, user, task, "2026-09-10")
    order.cancel()
    assert order.is_cancelled is True


def test_create_order():
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван", "iv@e.ru")
    task = CleaningTask(1, room, "2026-09-15")
    orders = []
    order = create_order(orders, user, task, "2026-09-10")
    assert order in orders
    assert len(orders) == 1


def test_find_orders_by_user():
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван", "iv@e.ru")
    task = CleaningTask(1, room, "2026-09-15")
    orders = []
    create_order(orders, user, task, "2026-09-10")
    assert len(find_orders_by_user(orders, 1)) == 1
    assert len(find_orders_by_user(orders, 2)) == 0


def test_find_orders_by_room():
    room = Room(1, "Аудитория 301", 30)
    user = User(1, "Иван", "iv@e.ru")
    task = CleaningTask(1, room, "2026-09-15")
    orders = []
    create_order(orders, user, task, "2026-09-10")
    assert len(find_orders_by_room(orders, 1)) == 1
    assert len(find_orders_by_room(orders, 2)) == 0

"""Тесты класса User."""
from models import User
from models.users import add_user, find_user


def test_user_creation():
    user = User(1, "Иван Петров", "ivan@example.com")
    assert user.id == 1
    assert user.name == "Иван Петров"
    assert user.email == "ivan@example.com"


def test_user_from_data():
    data = {"id": 1, "name": "Иван", "email": "iv@e.ru"}
    user = User.from_data(data)
    assert user.id == 1
    assert user.name == "Иван"


def test_add_user():
    users = []
    user = add_user(users, "Иван", "iv@e.ru")
    assert len(users) == 1
    assert user is users[0]


def test_find_user():
    users = []
    add_user(users, "Иван Петров", "ivan@example.com")
    add_user(users, "Анна Смирнова", "anna@example.com")
    result = find_user(users, "иван")
    assert len(result) == 1

"""Модель пользователя-заказчика уборки."""
from typing import List, Optional


class User:
    """Пользователь программы — заказчик уборки."""

    def __init__(
        self, user_id: int, name: str, email: str
    ) -> None:
        """Создать объект пользователя."""
        self.id = user_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"{self.name} ({self.email})"

    @classmethod
    def from_data(cls, data: dict) -> "User":
        """Создать пользователя из словаря JSON."""
        return cls(
            user_id=data["id"],
            name=data["name"],
            email=data["email"],
        )


def add_user(users: List[User], name: str, email: str) -> User:
    """Создать объект User и добавить в коллекцию."""
    user_id = len(users) + 1
    user = User(user_id, name, email)
    users.append(user)
    return user


def find_user(users: List[User], query: str) -> List[User]:
    """Найти пользователей по имени или email."""
    q = query.lower()
    return [
        u for u in users
        if q in u.name.lower() or q in u.email.lower()
    ]


def find_user_by_id(
    users: List[User], user_id: int
) -> Optional[User]:
    """Найти пользователя по ID."""
    for user in users:
        if user.id == user_id:
            return user
    return None


def show_users(users: List[User]) -> None:
    """Вывести список пользователей."""
    if not users:
        print("Список пользователей пуст.")
        return
    print(f"\n{'ID':<4}{'Имя':<25}{'Email':<30}")
    print("-" * 59)
    for u in users:
        print(f"{u.id:<4}{u.name:<25}{u.email:<30}")

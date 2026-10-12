"""Модель заказа на уборку."""
from typing import List, Optional
from .users import User
from .tasks import CleaningTask


class Order:
    """Заказ: пользователь оформил задачу уборки."""

    def __init__(
        self,
        order_id: int,
        user: User,
        task: CleaningTask,
        order_date: str,
    ) -> None:
        """Создать заказ на уборку."""
        self.id = order_id
        self.user = user
        self.task = task
        self.order_date = order_date
        self.is_cancelled = False

    def cancel(self) -> None:
        """Отменить заказ."""
        self.is_cancelled = True

    def __str__(self) -> str:
        status = "отменён" if self.is_cancelled else "активен"
        return (
            f"Заказ №{self.id} [{status}]\n"
            f"  Помещение: {self.task.room.name} "
            f"(вместимость {self.task.room.capacity} чел.)\n"
            f"  Дата задачи: {self.task.task_date}\n"
            f"  Дата оформления: {self.order_date}\n"
            f"  Описание задачи: {self.task.description}\n"
            f"  Заказчик: {self.user.name} <{self.user.email}>"
        )


def create_order(
    orders: List[Order],
    user: User,
    task: CleaningTask,
    order_date: str,
) -> Order:
    """Оформить заказ на задачу."""
    order_id = len(orders) + 1
    order = Order(order_id, user, task, order_date)
    orders.append(order)
    return order


def cancel_order(orders: List[Order], order_id: int) -> bool:
    """Отменить заказ по идентификатору."""
    for order in orders:
        if order.id == order_id:
            order.cancel()
            return True
    return False


def find_order_by_id(
    orders: List[Order], order_id: int
) -> Optional[Order]:
    """Найти заказ по идентификатору."""
    for order in orders:
        if order.id == order_id:
            return order
    return None


def find_orders_by_user(
    orders: List[Order], user_id: int
) -> List[Order]:
    """Найти все заказы пользователя."""
    return [o for o in orders if o.user.id == user_id]


def find_orders_by_room(
    orders: List[Order], room_id: int
) -> List[Order]:
    """Найти все заказы для помещения."""
    return [o for o in orders if o.task.room.id == room_id]


def show_orders(orders: List[Order]) -> None:
    """Вывести список заказов в консоль."""
    if not orders:
        print("Список заказов пуст.")
        return
    header = f"\n{'ID':<4}{'Помещение':<15}{'Вмест.':<8}"
    header += f"{'Дата задачи':<14}{'Оформлен':<14}"
    header += f"{'Заказчик':<18}{'Email':<25}{'Статус':<10}"
    print(header)
    print("-" * 108)
    for o in orders:
        status = "отменён" if o.is_cancelled else "активен"
        print(
            f"{o.id:<4}{o.task.room.name:<15}"
            f"{o.task.room.capacity:<8}"
            f"{o.task.task_date:<14}"
            f"{o.order_date:<14}"
            f"{o.user.name:<18}{o.user.email:<25}"
            f"{status:<10}"
        )
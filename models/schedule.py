"""Модель расписания уборки."""
from typing import List, Optional
from .rooms import Room
from .users import User
from .tasks import CleaningTask


class Schedule:
    """Запись расписания: задача, помещение, заказчик."""

    def __init__(
        self,
        schedule_id: int,
        task: CleaningTask,
        room: Room,
        user: User,
        scheduled_date: str,
    ) -> None:
        """Создать запись расписания."""
        self.id = schedule_id
        self.task = task
        self.room = room
        self.user = user
        self.scheduled_date = scheduled_date

    def __str__(self) -> str:
        return (
            f"Расписание №{self.id}: "
            f"{self.room.name} на {self.scheduled_date}, "
            f"заказчик: {self.user.name}, "
            f"задача №{self.task.id}"
        )


def add_schedule(
    schedules: List[Schedule],
    task: CleaningTask,
    room: Room,
    user: User,
    scheduled_date: str,
) -> Schedule:
    """Добавить запись расписания."""
    schedule_id = len(schedules) + 1
    record = Schedule(
        schedule_id, task, room, user, scheduled_date
    )
    schedules.append(record)
    return record


def find_schedule_by_id(
    schedules: List[Schedule], schedule_id: int
) -> Optional[Schedule]:
    """Найти запись расписания по ID."""
    for s in schedules:
        if s.id == schedule_id:
            return s
    return None


def find_schedules_by_user(
    schedules: List[Schedule], user_id: int
) -> List[Schedule]:
    """Найти все записи расписания для пользователя."""
    return [s for s in schedules if s.user.id == user_id]


def find_schedules_by_room(
    schedules: List[Schedule], room_id: int
) -> List[Schedule]:
    """Найти все записи расписания для помещения."""
    return [s for s in schedules if s.room.id == room_id]


def show_schedules(schedules: List[Schedule]) -> None:
    """Вывести расписание."""
    if not schedules:
        print("Расписание пусто.")
        return
    header = f"\n{'ID':<4}{'Помещение':<25}{'Дата':<15}"
    header += f"{'Заказчик':<20}{'Задача':<8}"
    print(header)
    print("-" * 72)
    for s in schedules:
        print(
            f"{s.id:<4}{s.room.name:<25}{s.scheduled_date:<15}"
            f"{s.user.name:<20}{s.task.id:<8}"
        )

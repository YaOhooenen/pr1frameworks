"""Модель задачи уборки."""
from typing import List, Optional
from .rooms import Room


class CleaningTask:
    """Задача уборки помещения."""

    def __init__(
        self,
        task_id: int,
        room: Room,
        task_date: str,
        description: str = "",
    ) -> None:
        """Создать задачу уборки."""
        self.id = task_id
        self.room = room
        self.task_date = task_date
        self.description = description
        self.is_cancelled = False

    def cancel(self) -> None:
        """Отменить задачу."""
        self.is_cancelled = True

    def __str__(self) -> str:
        status = "отменена" if self.is_cancelled else "активна"
        return (
            f"Задача №{self.id}: уборка {self.room.name} "
            f"на {self.task_date} [{status}]"
        )


def is_room_available(
    tasks: List[CleaningTask], room: Room, task_date: str
) -> bool:
    """Проверить, свободно ли помещение на дату."""
    for task in tasks:
        if (
            task.room.id == room.id
            and task.task_date == task_date
            and not task.is_cancelled
        ):
            return False
    return True


def create_task(
    tasks: List[CleaningTask],
    room: Room,
    task_date: str,
    description: str = "",
) -> Optional[CleaningTask]:
    """Создать задачу уборки, если помещение свободно."""
    if not is_room_available(tasks, room, task_date):
        return None
    task_id = len(tasks) + 1
    task = CleaningTask(task_id, room, task_date, description)
    tasks.append(task)
    return task


def cancel_task(tasks: List[CleaningTask], task_id: int) -> bool:
    """Отменить задачу по ID."""
    for task in tasks:
        if task.id == task_id:
            task.cancel()
            return True
    return False


def find_task_by_id(
    tasks: List[CleaningTask], task_id: int
) -> Optional[CleaningTask]:
    """Найти задачу по ID."""
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def get_task_status(is_available: bool) -> str:
    """Текстовый статус доступности."""
    if is_available:
        return "Помещение доступно для уборки"
    return "Помещение уже занято (задача назначена)"


def show_tasks(tasks: List[CleaningTask]) -> None:
    """Вывести список задач."""
    if not tasks:
        print("Список задач пуст.")
        return
    print(f"\n{'ID':<4}{'Помещение':<25}{'Дата':<15}{'Статус':<12}")
    print("-" * 56)
    for t in tasks:
        status = "отменена" if t.is_cancelled else "активна"
        print(
            f"{t.id:<4}{t.room.name:<25}"
            f"{t.task_date:<15}{status:<12}"
        )

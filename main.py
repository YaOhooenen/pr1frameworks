"""Система планирования уборки — точка запуска."""
from models.rooms import (
    add_room, find_room, check_room_capacity,
    show_rooms, find_room_by_id,
)
from models.users import (
    add_user, show_users, find_user_by_id,
)
from models.tasks import (
    is_room_available, create_task, cancel_task,
    get_task_status, show_tasks, find_task_by_id,
)
from models.schedule import (
    add_schedule, show_schedules,
    find_schedules_by_user, find_schedules_by_room,
)
from storage import (
    load_rooms, save_rooms,
    load_users, save_users,
    load_tasks, save_tasks,
    load_schedules, save_schedules,
)
from utils import input_int, input_date


def menu() -> None:
    """Вывести главное меню."""
    print("\n=== Система планирования уборки ===")
    print("1. Показать помещения")
    print("2. Добавить помещение")
    print("3. Найти помещение")
    print("4. Проверить вместимость")
    print("5. Показать пользователей")
    print("6. Добавить пользователя")
    print("7. Проверить доступность помещения")
    print("8. Создать задачу уборки")
    print("9. Отменить задачу")
    print("10. Показать все задачи")
    print("11. Составить расписание (заказ)")
    print("12. Показать расписание")
    print("13. Расписание по заказчику")
    print("14. Расписание по помещению")
    print("0. Выход")


def create_new_task(tasks, rooms):
    """Создать задачу уборки через диалог."""
    room_id = input_int("ID помещения: ")
    room = find_room_by_id(rooms, room_id)
    if room is None:
        print("Помещение не найдено.")
        return None
    task_date = input_date("Дата уборки (ДД.ММ.ГГГГ): ")
    description = input("Описание задачи: ")
    task = create_task(tasks, room, task_date, description)
    if task is None:
        print("Помещение занято на эту дату.")
        return None
    print(f"Задача №{task.id} создана.")
    return task


def create_new_schedule(schedules, tasks, rooms, users) -> None:
    """Пользовательский сценарий: заказчик заказывает уборку."""
    user_id = input_int("ID заказчика: ")
    user = find_user_by_id(users, user_id)
    if user is None:
        print("Пользователь не найден.")
        return

    room_id = input_int("ID помещения: ")
    room = find_room_by_id(rooms, room_id)
    if room is None:
        print("Помещение не найдено.")
        return

    task_id = input_int("ID задачи: ")
    task = find_task_by_id(tasks, task_id)
    if task is None:
        print("Задача не найдена.")
        return

    scheduled_date = input_date("Дата по расписанию (ДД.ММ.ГГГГ): ")
    record = add_schedule(schedules, task, room, user, scheduled_date)
    print(f"Расписание №{record.id} создано.")


def main() -> None:
    """Точка запуска приложения."""
    rooms = load_rooms()
    users = load_users()
    tasks = load_tasks(rooms)
    schedules = load_schedules(rooms, users, tasks)

    while True:
        menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            show_rooms(rooms)
        elif choice == "2":
            name = input("Название: ")
            cap = input_int("Вместимость: ")
            add_room(rooms, name, cap)
            save_rooms(rooms)
        elif choice == "3":
            query = input("Подстрока: ")
            show_rooms(find_room(rooms, query))
        elif choice == "4":
            rid = input_int("ID помещения: ")
            mc = input_int("Мин. вместимость: ")
            if check_room_capacity(rooms, rid, mc):
                print("Подходит.")
            else:
                print("Не подходит.")
        elif choice == "5":
            show_users(users)
        elif choice == "6":
            name = input("Имя: ")
            email = input("Email: ")
            add_user(users, name, email)
            save_users(users)
        elif choice == "7":
            rid = input_int("ID помещения: ")
            room = find_room_by_id(rooms, rid)
            if room:
                d = input_date("Дата (ДД.ММ.ГГГГ): ")
                status = is_room_available(tasks, room, d)
                print(get_task_status(status))
        elif choice == "8":
            create_new_task(tasks, rooms)
            save_tasks(tasks)
        elif choice == "9":
            tid = input_int("ID задачи: ")
            if cancel_task(tasks, tid):
                save_tasks(tasks)
                print("Задача отменена.")
            else:
                print("Задача не найдена.")
        elif choice == "10":
            show_tasks(tasks)
        elif choice == "11":
            create_new_schedule(schedules, tasks, rooms, users)
            save_schedules(schedules)
        elif choice == "12":
            show_schedules(schedules)
        elif choice == "13":
            uid = input_int("ID заказчика: ")
            found = find_schedules_by_user(schedules, uid)
            show_schedules(found)
        elif choice == "14":
            rid = input_int("ID помещения: ")
            found = find_schedules_by_room(schedules, rid)
            show_schedules(found)
        elif choice == "0":
            save_rooms(rooms)
            save_users(users)
            save_tasks(tasks)
            save_schedules(schedules)
            print("Выход.")
            break
        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    main()

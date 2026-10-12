"""Система планирования уборки — точка запуска."""
from models.rooms import (
    add_room, find_room, check_room_capacity,
    sort_rooms_by_capacity, show_rooms, find_room_by_id,
)
from models.users import (
    add_user, find_user, show_users, find_user_by_id,
)
from models.tasks import (
    is_room_available, create_task, cancel_task,
    get_task_status, show_tasks, find_task_by_id,
)
from models.orders import (
    create_order, cancel_order, show_orders,
    find_orders_by_user, find_orders_by_room,
)
from storage import (
    load_rooms, save_rooms,
    load_users, save_users,
    load_tasks, save_tasks,
    load_orders, save_orders,
)
from utils import input_int, input_date


def menu() -> None:
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
    print("11. Оформить заказ на задачу")
    print("12. Отменить заказ")
    print("13. Показать все заказы")
    print("14. Заказы по заказчику")
    print("15. Заказы по помещению")
    print("16. Помещения по вместимости")
    print("0. Выход")


def create_new_task(tasks, rooms):
    """Создать задачу уборки."""
    rid = input_int("ID помещения: ")
    room = find_room_by_id(rooms, rid)
    if room is None:
        print("Помещение не найдено.")
        return None
    d = input_date("Дата уборки (ДД.ММ.ГГГГ): ")
    desc = input("Описание задачи: ")
    task = create_task(tasks, room, d, desc)
    if task is None:
        print("Помещение занято на эту дату.")
        return None
    print(f"Задача №{task.id} создана.")
    return task


def create_new_order(orders, users, tasks):
    """Оформить заказ на существующую задачу."""
    uid = input_int("ID заказчика: ")
    user = find_user_by_id(users, uid)
    if user is None:
        print("Пользователь не найден.")
        return

    tid = input_int("ID задачи: ")
    task = find_task_by_id(tasks, tid)
    if task is None:
        print("Задача не найдена.")
        return

    d = input_date("Дата оформления заказа (ДД.ММ.ГГГГ): ")
    order = create_order(orders, user, task, d)
    print(f"Заказ №{order.id} оформлен.")
    print(order)


def main() -> None:
    rooms = load_rooms()
    users = load_users()
    tasks = load_tasks(rooms)
    orders = load_orders(users, tasks)

    while True:
        menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            show_rooms(rooms)
        elif choice == "2":
            add_room(rooms, input("Название: "),
                     input_int("Вместимость: "))
            save_rooms(rooms)
        elif choice == "3":
            show_rooms(find_room(rooms, input("Подстрока: ")))
        elif choice == "4":
            rid = input_int("ID помещения: ")
            mc = input_int("Мин. вместимость: ")
            print("Подходит." if check_room_capacity(rooms, rid, mc)
                  else "Не подходит.")
        elif choice == "5":
            show_users(users)
        elif choice == "6":
            add_user(users, input("Имя: "), input("Email: "))
            save_users(users)
        elif choice == "7":
            rid = input_int("ID помещения: ")
            room = find_room_by_id(rooms, rid)
            if room:
                d = input_date("Дата (ДД.ММ.ГГГГ): ")
                print(get_task_status(
                    is_room_available(tasks, room, d)))
        elif choice == "8":
            create_new_task(tasks, rooms)
            save_tasks(tasks)
        elif choice == "9":
            tid = input_int("ID задачи: ")
            if cancel_task(tasks, tid):
                save_tasks(tasks)
                print("Задача отменена.")
        elif choice == "10":
            show_tasks(tasks)
        elif choice == "11":
            create_new_order(orders, users, tasks)
            save_orders(orders)
        elif choice == "12":
            oid = input_int("ID заказа: ")
            if cancel_order(orders, oid):
                save_orders(orders)
                print("Заказ отменён.")
        elif choice == "13":
            show_orders(orders)
        elif choice == "14":
            uid = input_int("ID заказчика: ")
            show_orders(find_orders_by_user(orders, uid))
        elif choice == "15":
            rid = input_int("ID помещения: ")
            show_orders(find_orders_by_room(orders, rid))
        elif choice == "16":
            show_rooms(sort_rooms_by_capacity(rooms))
        elif choice == "0":
            save_rooms(rooms)
            save_users(users)
            save_tasks(tasks)
            save_orders(orders)
            print("Выход.")
            break
        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    main()

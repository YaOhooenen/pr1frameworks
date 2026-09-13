from datetime import date, datetime


admin_name = "Анна Петрова"
room_name = "Аудитория 301"
room_capacity = 30
cleaning_date_str = "2026-09-15"  
is_room_occupied = False
assigned_user = "Иван Смирнов"



def check_room_availability(is_occupied, room_name):
    if not is_occupied:
        return f"Помещение '{room_name}' свободно для уборки."
    else:
        return f"Помещение '{room_name}' занято. Уборка невозможна."

def assign_task(user, room):
    return f"Задача по уборке помещения '{room}' назначена на сотрудника: {user}."

def calculate_cleaning_time(capacity):
    time_minutes = float(capacity) * 1.5 
    return f"Примерное время уборки: {time_minutes:.0f} минут."



print("=== Система планирования уборки ===")
print(f"Администратор: {admin_name}")


try:
    cleaning_date = datetime.strptime(cleaning_date_str, "%Y-%m-%d").date()
    print(f"Дата уборки: {cleaning_date}")
except ValueError:
    print("Ошибка формата даты.")


print("-" * 30)
print(check_room_availability(is_room_occupied, room_name))

if not is_room_occupied:
    print(assign_task(assigned_user, room_name))
    print(calculate_cleaning_time(room_capacity))
else:
    print("Попробуйте выбрать другое время или помещение.")
print("-" * 30)
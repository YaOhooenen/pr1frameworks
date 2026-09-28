"""Вспомогательные функции для ввода данных с обработкой ошибок."""
from datetime import datetime


def input_int(prompt: str) -> int:
    """Запросить у пользователя целое число с повторным вводом при ошибке."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: необходимо ввести целое число. Попробуйте снова.")


def input_date(prompt: str) -> str:
    """Запросить у пользователя дату в формате ДД.ММ.ГГГГ."""
    while True:
        raw = input(prompt)
        try:
            parsed = datetime.strptime(raw, "%d.%m.%Y")
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            print("Ошибка: неверный формат даты. Используйте ДД.ММ.ГГГГ.")

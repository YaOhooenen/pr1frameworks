# Система планирования уборки

Консольное и веб-приложение для планирования уборки помещений.
Пользователь-заказчик оформляет задачу уборки, привязывая её к помещению
и дате; задачи, заказы и пользователи отображаются через веб-интерфейс.

## 1. Назначение

Приложение автоматизирует планирование уборки:
- учёт помещений и их вместимости;
- учёт пользователей-заказчиков;
- создание задач уборки и их отмена;
- оформление заказов (кто и когда заказал задачу);
- отображение данных через веб-интерфейс на Django.

## 2. Технологии

- Python 3.11
- Django 5.2
- Django Template Language (DTL)
- HTML5, CSS3, JavaScript
- Bootstrap 5.3
- JSON (хранение данных)
- pytest (тесты)
- flake8 (линтер)
- Git

## 3. Предметная область

Основные сущности:

- Room — помещение: id, name, capacity;
- User — заказчик: id, name, email;
- CleaningTask — задача уборки: id, room, task_date,
  description, is_cancelled;
- Order — заказ: id, user, task, order_date, is_cancelled.

Связи:

- Order ссылается на User и CleaningTask;
- CleaningTask ссылается на Room.

На текущем этапе данные хранятся в JSON-файлах, Django ORM не используется.

## 4. Структура проекта

    pr1frameworks/
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    ├── main.py
    ├── storage.py
    ├── utils.py
    ├── conftest.py
    ├── pytest.ini
    ├── .flake8
    ├── roomly/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── templates/
    │   ├── base.html
    │   └── includes/
    │       └── navigation.html
    ├── homepage/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── migrations/
    │   ├── templates/
    │   │   └── homepage/
    │   │       ├── index.html
    │   │       └── 404.html
    │   └── static/
    │       └── homepage/
    │           ├── css/
    │           │   └── style.css
    │           ├── js/
    │           │   └── main.js
    │           └── img/
    │               └── logo.png
    ├── rooms/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── migrations/
    │   └── templates/
    │       └── rooms/
    │           ├── room_list.html
    │           ├── room_detail.html
    │           └── includes/
    │               └── room_card.html
    ├── tasks/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── migrations/
    │   └── templates/
    │       └── tasks/
    │           ├── task_list.html
    │           ├── task_detail.html
    │           └── includes/
    │               └── task_status.html
    ├── orders/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── migrations/
    │   └── templates/
    │       └── orders/
    │           ├── order_list.html
    │           ├── order_detail.html
    │           └── includes/
    │               └── order_status.html
    ├── users/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── migrations/
    │   └── templates/
    │       └── users/
    │           ├── user_list.html
    │           └── user_detail.html
    ├── models/
    │   ├── __init__.py
    │   ├── rooms.py
    │   ├── users.py
    │   ├── tasks.py
    │   └── orders.py
    ├── data/
    │   ├── rooms.json
    │   ├── users.json
    │   ├── tasks.json
    │   └── orders.json
    └── tests/
        ├── test_rooms.py
        ├── test_users.py
        ├── test_tasks.py
        └── test_orders.py

## 5. Веб-интерфейс

Реализованные страницы:

- / — главная;
- /rooms/ — список помещений;
- /rooms/<int:room_id>/ — карточка помещения;
- /tasks/ — список задач;
- /tasks/<int:task_id>/ — карточка задачи;
- /orders/ — список заказов;
- /orders/<int:order_id>/ — карточка заказа;
- /users/ — список пользователей;
- /users/<int:user_id>/ — карточка пользователя.

Формирование HTML вынесено в Django-шаблоны.
Функция page() не используется.

## 6. Django Template Language

В шаблонах используются:

- {% extends "base.html" %} — наследование базового шаблона;
- {% block title %} и {% block content %} — переопределение блоков;
- {% include %} — подключение частей шаблона
  (navigation.html, room_card.html, task_status.html,
  order_status.html);
- {{ переменная }} — вывод значений;
- {% for %} и {% empty %} — циклы и обработка пустой коллекции;
- {% if %} и {% else %} — условное отображение;
- {% url %} — именованные маршруты с пространствами имён.

Пространства имён и имена маршрутов:

- homepage:index;
- rooms:list, rooms:detail;
- tasks:list, tasks:detail;
- orders:list, orders:detail;
- users:list, users:detail.

Используемые фильтры шаблонов:

- {{ rooms|length }}, {{ tasks|length }}, {{ orders|length }},
  {{ users|length }} — количество элементов;
- {{ room.name|default:"Без названия" }},
  {{ task.description|default:"—" }} — значения по умолчанию.

## 7. Статические файлы

Расположены в приложении homepage:

    homepage/static/homepage/
    ├── css/style.css
    ├── js/main.js
    └── img/logo.png

Подключение выполняется через {% load static %} и
{% static '...' %}. JavaScript устанавливает текущий год
в подвале страницы.

## 8. Хранение данных

Данные приложения хранятся в JSON-файлах в каталоге data/:

- rooms.json — помещения;
- users.json — пользователи;
- tasks.json — задачи уборки;
- orders.json — заказы.

Загрузка и сохранение — в модуле storage.py.
Классы предметной области — в пакете models/.
Django ORM на текущем этапе не используется.

## 9. Установка и запуск

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Открыть в браузере: http://127.0.0.1:8000/.

Консольная версия (сохранена с ПР3):

    python main.py

## 10. Тестирование и проверка качества кода

    pytest -v
    flake8

## 11. Дальнейшее развитие

- переход от JSON к базе данных и Django ORM;
- Django Forms для создания и редактирования объектов;
- регистрация и аутентификация пользователей;
- REST API;
- контейнеризация (Docker);
- CI/CD.
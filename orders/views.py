"""View-функции приложения заказов."""
from django.shortcuts import render
from models.orders import find_order_by_id
from storage import (
    load_orders, load_rooms, load_users, load_tasks,
)


def _load_all():
    """Загрузить заказы со связанными объектами."""
    rooms = load_rooms()
    users = load_users()
    tasks = load_tasks(rooms)
    return load_orders(users, tasks)


def orders(request):
    """Список заказов."""
    context = {"orders": _load_all()}
    return render(request, "orders/order_list.html", context)


def order_detail(request, order_id):
    """Страница заказа."""
    order = find_order_by_id(_load_all(), order_id)
    context = {"order": order}
    return render(
        request,
        "orders/order_detail.html",
        context,
        status=404 if order is None else 200,
    )

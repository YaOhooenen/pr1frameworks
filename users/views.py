"""View-функции приложения пользователей."""
from django.shortcuts import render
from models.users import find_user_by_id
from storage import load_users


def _load_users():
    """Загрузить пользователей."""
    return load_users()


def users(request):
    """Список пользователей."""
    context = {"users": _load_users()}
    return render(request, "users/user_list.html", context)


def user_detail(request, user_id):
    """Страница пользователя."""
    user = find_user_by_id(_load_users(), user_id)
    context = {"user": user}
    return render(
        request,
        "users/user_detail.html",
        context,
        status=404 if user is None else 200,
    )
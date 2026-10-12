"""View-функции приложения задач."""
from django.shortcuts import render
from models.tasks import find_task_by_id
from storage import load_rooms, load_tasks


def _load_tasks():
    """Загрузить задачи со связанными помещениями."""
    rooms = load_rooms()
    return load_tasks(rooms)


def tasks(request):
    """Список задач."""
    context = {"tasks": _load_tasks()}
    return render(request, "tasks/task_list.html", context)


def task_detail(request, task_id):
    """Страница задачи."""
    task = find_task_by_id(_load_tasks(), task_id)
    context = {"task": task}
    return render(
        request,
        "tasks/task_detail.html",
        context,
        status=404 if task is None else 200,
    )

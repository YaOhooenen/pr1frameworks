"""Корневая маршрутизация проекта."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("rooms/", include("rooms.urls")),
    path("tasks/", include("tasks.urls")),
    path("orders/", include("orders.urls")),
    path("users/", include("users.urls")),
]

handler404 = "homepage.views.page_not_found"
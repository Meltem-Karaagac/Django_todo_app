from django.urls import path
from .views import home, todo_list, todo_create, todo_update, todo_delete

urlpatterns = [
    path("", home, name="house"),
    path("list/", todo_list, name="todo-list"),
    path("create/", todo_create, name="todo-create"),
    path("<int:id>/update/", todo_update, name="todo-update"),
    path("<int:id>/delete/", todo_delete, name="todo-delete")
]

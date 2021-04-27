from django.urls import path

from .views import TodoCreateView, TodoListView

urlpatterns = [
    path("todos/", TodoCreateView.as_view(), name="todo-create"),
    path("todos/", TodoListView.as_view(), name="todo-list"),
]

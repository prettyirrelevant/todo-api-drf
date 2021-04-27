from django.urls import path

from .views import TodoCreateListView

urlpatterns = [
    path("todos/", TodoCreateListView.as_view(), name="todo-create-list"),
]

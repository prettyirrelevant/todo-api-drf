from django.urls import path

from .views import TodoCreateListView, TodoRetrieveUpdateDeleteView

urlpatterns = [
    path("todos/", TodoCreateListView.as_view(), name="todo-create-list"),
    path(
        "todo/<uuid>/", TodoRetrieveUpdateDeleteView.as_view(), name="todo-retrieve-update-delete"
    ),
]

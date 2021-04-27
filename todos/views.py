from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


class TodoCreateView(CreateAPIView):
    """
    Creates new todo.
    """

    queryset = Todo
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            data={"message": "Todo created successfully!", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

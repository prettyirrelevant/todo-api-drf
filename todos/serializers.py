from rest_framework.serializers import ModelSerializer

from .models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ["uuid", "content", "is_complete", "timestamp"]
        extra_kwargs = {"uuid": {"read_only": True}, "timestamp": {"read_only": True}}

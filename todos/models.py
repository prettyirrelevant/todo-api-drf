import uuid

from django.db import models


class Todo(models.Model):
    uuid = models.UUIDField("uuid", default=uuid.uuid4, editable=False)
    content = models.CharField("Content", max_length=150, blank=False, null=False)
    is_complete = models.BooleanField("Is Complete", default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

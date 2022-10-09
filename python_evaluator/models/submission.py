import uuid
from django.db import models

from .environment import PythonEnvironment


class PythonSubmission(models.Model):
    class Meta:
        db_table = "python_submissions"

    source_code = models.TextField()
    environment = models.ForeignKey(PythonEnvironment, on_delete=models.PROTECT)
    output = models.TextField(null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)
    slug = models.UUIDField(default=uuid.uuid4)

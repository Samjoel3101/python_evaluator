from uuid import uuid4
from django.db import models

from .environment import PythonEnvironment


def upload_expected_output(instance, filename):
    return f"question_{instance.slug}/expected_output.txt"


class PythonQuestion(models.Model):
    class Meta:
        db_table = "python_questions"

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    environment = models.ForeignKey(PythonEnvironment, on_delete=models.PROTECT)
    expected_output = models.FileField(null=True, blank=True)
    slug = models.UUIDField(default=uuid4)

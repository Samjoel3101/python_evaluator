from django.db import models

from .base import BaseModel
from .environment import PythonEnvironment


def upload_environment_file(instance, filename):
    return f"environment_{instance.environment.slug}/files/{filename}"


class EnvironmentFile(BaseModel):
    class Meta:
        db_table = "environment_files"

    environment = models.ForeignKey(PythonEnvironment, on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_environment_file)

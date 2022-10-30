from django.db import models
from django.core.validators import FileExtensionValidator
from django_mysql.models.fields import EnumField

import uuid


def upload_environment(instance, filename):
    return f"environment_{instance.slug}/requirements.txt"


class PythonVersionType(models.TextChoices):
    PYTHON36 = "3.6"
    PYTHON37 = "3.7"
    PYTHON38 = "3.8"


class PythonEnvironmentStatusType(models.TextChoices):
    QUEUED = "queued"
    BUILDING = "building"
    COMPLETED = "completed"
    ERROR = "error"


class PythonEnvironment(models.Model):
    class Meta:
        db_table = "python_environments"

    name = models.CharField(max_length=255)
    requirements_file = models.FileField(upload_to=upload_environment, validators=[FileExtensionValidator(["txt"])])
    status = EnumField(choices=PythonEnvironmentStatusType.choices, default=PythonEnvironmentStatusType.QUEUED)
    python_version = EnumField(choices=PythonVersionType.choices)
    slug = models.UUIDField(default=uuid.uuid4)
    docker_image = models.CharField(max_length=512, null=True, blank=True)
    build_logs = models.TextField(null=True, blank=True)
    build_commands = models.TextField(null=True, blank=True)
    meta_data = models.JSONField(null=True, blank=True)

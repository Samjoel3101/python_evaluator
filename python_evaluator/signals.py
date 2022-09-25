from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from python_evaluator.models import PythonEnvironment
from python_evaluator.models.environment import PythonEnvironmentStatusType
from python_evaluator.tasks import build_environment_container


@receiver(post_save, sender=PythonEnvironment)
def build_environment_image(sender, instance, created, *args, **kwargs):
    if created or instance.status not in [
        PythonEnvironmentStatusType.COMPLETED,
        PythonEnvironmentStatusType.BUILDING,
        PythonEnvironmentStatusType.ERROR,
    ]:
        transaction.on_commit(lambda: build_environment_container.delay(instance.id))

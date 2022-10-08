import json
from celery import shared_task

from python_evaluator.models import PythonEnvironment
from python_evaluator.models.environment import PythonEnvironmentStatusType
from python_evaluator.utils.build_container import build_docker_image


def get_docker_image_name(environment):
    return f"{environment.id}_{environment.name.lower()}"


def update_python_environment_status(environment, status, commit=True):
    environment.status = status
    if commit:
        environment.save(update_fields=["status"])


@shared_task
def build_environment_container(environment_id: int):
    environment = PythonEnvironment.objects.get(id=environment_id)
    docker_image_name = get_docker_image_name(environment)
    update_python_environment_status(environment, PythonEnvironmentStatusType.BUILDING)
    logs = build_docker_image(environment.requirements_file.file.read(), environment.python_version, docker_image_name)
    environment.build_logs = json.dumps(logs)
    if logs["error"]:
        update_python_environment_status(environment, PythonEnvironmentStatusType.ERROR, commit=False)
    else:
        environment.docker_image = docker_image_name
        update_python_environment_status(environment, PythonEnvironmentStatusType.COMPLETED, commit=False)

    environment.save(update_fields=["status", "docker_image", "build_logs"])

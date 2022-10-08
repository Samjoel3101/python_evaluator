from rest_framework import serializers

from python_evaluator.models import PythonEnvironment


class BasePythonEnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonEnvironment
        fields = ["id", "slug", "name", "python_version"]

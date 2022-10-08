from rest_framework import serializers

from python_evaluator.models import PythonQuestionSubmission
from python_evaluator.serializers.environment import BasePythonEnvironmentSerializer


class BasePythonQuestionSubmissionSerializer(serializers.ModelSerializer):
    environment = BasePythonEnvironmentSerializer(read_only=True)

    class Meta:
        model = PythonQuestionSubmission
        fields = ["id", "environment", "slug"]

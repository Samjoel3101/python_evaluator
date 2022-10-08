from rest_framework import serializers

from .base import BasePythonQuestionSubmissionSerializer
from python_evaluator.serializers.environment import ListPythonEnvironmentSerializer


class ListPythonQuestionSubmissionSerializer(BasePythonQuestionSubmissionSerializer):
    url = serializers.SerializerMethodField()
    environment = ListPythonEnvironmentSerializer(read_only=True)

    class Meta(BasePythonQuestionSubmissionSerializer):
        fields = BasePythonQuestionSubmissionSerializer.Meta.fields + ["url"]

    def get_url(self, submission):
        return None

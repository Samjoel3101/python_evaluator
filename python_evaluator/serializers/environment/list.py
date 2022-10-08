from rest_framework import serializers

from .base import BasePythonEnvironmentSerializer


class ListPythonEnvironmentSerializer(BasePythonEnvironmentSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta(BasePythonEnvironmentSerializer.Meta):
        fields = BasePythonEnvironmentSerializer.Meta.fields + ["url"]

    def get_url(self, environment):
        return None

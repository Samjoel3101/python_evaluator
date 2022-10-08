from .list import ListPythonEnvironmentSerializer


class DetailPythonEnvironmentSerializer(ListPythonEnvironmentSerializer):
    class Meta(ListPythonEnvironmentSerializer.Meta):
        fields = ListPythonEnvironmentSerializer.Meta.fields + [
            "requirements_file",
            "docker_image",
            "build_logs",
            "meta_data",
        ]

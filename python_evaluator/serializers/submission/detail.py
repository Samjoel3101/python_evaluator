from .list import ListPythonQuestionSubmissionSerializer

from python_evaluator.serializers.environment import DetailPythonEnvironmentSerializer


class DetailPythonQuestionSubmissionSerializer(ListPythonQuestionSubmissionSerializer):
    environment = DetailPythonEnvironmentSerializer(read_only=True)

    class Meta(ListPythonQuestionSubmissionSerializer.Meta):
        fields = ListPythonQuestionSubmissionSerializer.Meta.fields + ["time", "source_code", "output"]

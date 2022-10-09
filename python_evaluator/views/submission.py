from rest_framework import viewsets, mixins

from python_evaluator.models import PythonSubmission
from python_evaluator.serializers import (
    ListPythonQuestionSubmissionSerializer,
    DetailPythonQuestionSubmissionSerializer,
)


class PythonSubmissionViewset(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    def get_queryset(self):
        return PythonSubmission.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ListPythonQuestionSubmissionSerializer
        return DetailPythonQuestionSubmissionSerializer

from rest_framework import viewsets, mixins

from python_evaluator.models import PythonEnvironment
from python_evaluator.serializers import DetailPythonEnvironmentSerializer, ListPythonEnvironmentSerializer


class PythonEnvironmentViewset(
    mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    lookup_field = "slug"

    def get_queryset(self):
        return PythonEnvironment.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ListPythonEnvironmentSerializer
        return DetailPythonEnvironmentSerializer

from rest_framework import routers

from django.urls import path, include
from python_evaluator.views import PythonEnvironmentViewset, PythonSubmissionViewset

app_name = "python_evaluator"
router = routers.DefaultRouter()

router.register("environments", PythonEnvironmentViewset, basename="environment")
router.register("submissions", PythonSubmissionViewset, basename="submission")

urlpatterns = [
    path("api/", include((router.urls, app_name), namespace="api")),
]

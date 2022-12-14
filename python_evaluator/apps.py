from django.apps import AppConfig


class PythonEvaluatorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "python_evaluator"

    def ready(self):
        import python_evaluator.signals

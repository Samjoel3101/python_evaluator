from django.contrib import admin

from python_evaluator.models import PythonEnvironment, PythonQuestionSubmission

admin.site.register(PythonEnvironment)
admin.site.register(PythonQuestionSubmission)

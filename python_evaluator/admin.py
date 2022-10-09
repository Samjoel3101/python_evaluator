from django.contrib import admin

from python_evaluator.models import PythonEnvironment, PythonSubmission

admin.site.register(PythonEnvironment)
admin.site.register(PythonSubmission)

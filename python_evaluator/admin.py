from django.contrib import admin

from python_evaluator.models import PythonEnvironment, PythonQuestion, PythonQuestionSubmission

admin.site.register(PythonEnvironment)
admin.site.register(PythonQuestion)
admin.site.register(PythonQuestionSubmission)

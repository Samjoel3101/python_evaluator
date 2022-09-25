from django.db import models

from .question import PythonQuestion


class PythonQuestionSubmission(models.Model):
    class Meta:
        db_table = "python_question_submissions"

    source_code = models.TextField()
    python_question = models.ForeignKey(PythonQuestion, on_delete=models.CASCADE)
    output = models.TextField(null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)

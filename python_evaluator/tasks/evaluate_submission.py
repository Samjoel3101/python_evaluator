from celery import shared_task

from python_evaluator.models import PythonQuestionSubmission
from python_evaluator.utils.run_python_code import run_python_code


@shared_task
def evaluate_submission(submission_id: int):
    submission = PythonQuestionSubmission.objects.get(id=submission_id)
    environment = submission.environment

    output, time = run_python_code(environment.docker_image, source_code=submission.source_code)
    print(output, time)

    submission.output = output
    submission.time = time
    submission.save(update_fields=["output", "time"])

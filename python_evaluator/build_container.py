import tempfile
import os
from io import BytesIO

from docker import APIClient


dockerfile = """FROM python:{python_version}-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

CMD ["python3", "/main.py"]

"""


def build_docker_image(dockerfile):
    client = APIClient(base_url="unix://var/run/docker.sock")

    requirements_txt = open("./requirements.txt", "r").read()
    print(dockerfile.format(python_version="3.8"))
    docker_file = BytesIO(dockerfile.format(python_version="3.8").encode("utf-8"))

    with tempfile.TemporaryDirectory() as tempdir:
        with open(os.path.join(tempdir, "requirements.txt"), "w+") as f:
            f.write(requirements_txt)
        with open(os.path.join(tempdir, "Dockerfile"), "wb") as d:
            d.write(docker_file.read())
            docker_file.seek(0)
        log_stream = client.build(path=tempdir, tag="sample-build:1.0", decode=True)

        for chunk in log_stream:
            if "stream" in chunk:
                print(chunk["stream"], end="")


build_docker_image(dockerfile)

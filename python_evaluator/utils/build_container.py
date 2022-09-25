import logging
import tempfile
import json
import os
from io import BytesIO

from docker import APIClient


dockerfile = """FROM python:{python_version}-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

CMD ["python3", "/main.py"]

"""


def build_docker_image(requirements_txt: bytes, python_version: str, image_name: "str"):
    client = APIClient(base_url="unix://var/run/docker.sock")
    logs = {"info": [], "error": []}

    docker_file = BytesIO(dockerfile.format(python_version=python_version).encode("utf-8"))

    with tempfile.TemporaryDirectory() as tempdir:
        with open(os.path.join(tempdir, "requirements.txt"), "wb") as f:
            f.write(requirements_txt)
        with open(os.path.join(tempdir, "Dockerfile"), "wb") as d:
            d.write(docker_file.read())

        log_stream = client.build(path=tempdir, tag=image_name, decode=True)
        for chunk in log_stream:
            if "stream" in chunk:
                chunk = chunk["stream"]
                # logging.info(chunk)
                logs["info"].append(chunk)
            elif ("error" or "errorDetail") in chunk.keys():
                print(chunk)
                # print(chunk)
                logs["error"].append(json.dumps(chunk))

    logs["info"] = "".join(logs["info"])
    logs["error"] = "".join(logs["error"])

    return logs

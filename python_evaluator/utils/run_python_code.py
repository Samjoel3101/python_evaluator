import subprocess
import tempfile
import os
import time


def run_python_code(docker_image: str, source_code: str):
    with tempfile.TemporaryDirectory() as tempdir:
        py_file_path = os.path.join(tempdir, "main.py")
        with open(py_file_path, "w+") as py_file:
            py_file.write(source_code)

        start_time = time.time()
        output = None
        try:
            output = subprocess.check_output(
                f"docker run --rm -v {py_file_path}:/main.py {docker_image}", shell=True, stderr=subprocess.STDOUT
            )
        except subprocess.CalledProcessError as e:
            output = e.output
        end_time = time.time()
        return output, int(end_time - start_time)

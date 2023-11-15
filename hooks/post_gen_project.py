import os
import sys
import subprocess

required_vars = (
    "{{ cookiecutter.db_user }}",
    "{{ cookiecutter.db_pass }}",
    "{{ cookiecutter.db_host }}",
    "{{ cookiecutter.db_port }}",
)

if None in required_vars:
    print("Some required values are missing please check inputs.")
    sys.exit(1)
else:
    project_directory = os.getcwd()

    subprocess.run(["python", "-m", "venv", "venv"], cwd=project_directory, check=True)
    subprocess.run(["bash", "../scripts/run_venv.sh"], cwd=project_directory, check=True)
    subprocess.run(["pip", "install", "-r", "requirements.txt"], cwd=project_directory, check=True)

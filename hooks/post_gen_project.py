import os
import subprocess

project_directory = os.getcwd()

subprocess.run(["python", "-m", "venv", "venv"], cwd=project_directory, check=True)
subprocess.run(["bash", "../scripts/run_venv.sh"], cwd=project_directory, check=True)
subprocess.run(["pip", "install", "-r", "requirements.txt"], cwd=project_directory, check=True)

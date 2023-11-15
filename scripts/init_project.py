import os
import subprocess

project_directory = "{{ cookiecutter.project_name }}"

subprocess.run(["python", "-m", "venv", "venv"], cwd=project_directory, check=True)

activate_script = os.path.join(project_directory, "venv", "bin", "activate")
activate_command = f"source {activate_script}"
subprocess.run(activate_command, shell=True, check=True)

requirements_file = os.path.join(project_directory, "requirements.txt")
install_command = ["pip", "install", "-r", requirements_file]
subprocess.run(install_command, cwd=project_directory, check=True)

print("Projeto inicializado com sucesso!")

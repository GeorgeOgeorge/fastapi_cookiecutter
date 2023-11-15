# define versão do linux
FROM python:3.11-alpine

RUN apk update && apk --no-cache add postgresql-dev gcc musl-dev

WORKDIR /{{cookiecutter.project_name}}

ADD . /{{cookiecutter.project_name}}

RUN pip install --no-cache-dir --upgrade -r /{{cookiecutter.project_name}}/requirements.txt

CMD ["python", "./run.py"]

from fastapi import APIRouter, status

from app.{{cookiecutter.module}}.utils.schemas import Post{{cookiecutter.module}}

{{cookiecutter.module}}_router = APIRouter(prefix="/{{cookiecutter.module}}")


@{{cookiecutter.module}}_router.post(path="/", status_code=status.HTTP_201_CREATED)
async def create_{{cookiecutter.module}}_route(payload: Post{{cookiecutter.module}}):
    return {"msg": "hi"}


@{{cookiecutter.module}}_router.put(path="/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_{{cookiecutter.module}}_route(id: int):
    return {"msg": id}


@{{cookiecutter.module}}_router.delete(path="/{id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_{{cookiecutter.module}}_route(id: int):
    return {"msg": id}


@{{cookiecutter.module}}_router.get(path="/", status_code=status.HTTP_200_OK)
@{{cookiecutter.module}}_router.get(path="/{id}", status_code=status.HTTP_200_OK)
async def list_{{cookiecutter.module}}_route(id: int | None):
    return {"msg": id or "hi"}

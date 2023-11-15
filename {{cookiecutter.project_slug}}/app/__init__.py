import asyncio
import logging
from http import HTTPStatus
from typing import Callable

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import declarative_base

from app.config import get_settings
from app.database.db_factory import DatabaseManager

base = declarative_base()
app_settings = get_settings()
db_manager = DatabaseManager(main_db="alfred", db_url=app_settings.database_url)
logger = logging.getLogger("app")


def create_app():
    """Creates app, register routers, define routines and middleware to validate token

    Returns:
        FastAPI: Created app
    """
    from app.{{ cookiecutter.module }}.routes import {{ cookiecutter.module }}_router
    from app.{{ cookiecutter.module }}.routines import {{ cookiecutter.module }}_routine

    app = FastAPI()
    app.include_router({{ cookiecutter.module }}_router)

    @app.on_event("startup")
    async def start_routines() -> None:
        """Defines routines to be executed in the background"""
        asyncio.create_task({{ cookiecutter.module }}_routine())

    @app.middleware("http")
    async def check_app_token(request: Request, call_next: Callable) -> Response:
        """Checks if all requests passed to the microservice have the app communication token

        Args:
            request (Request): current request
            call_next (Callable): route that would originally be called

        Returns:
            Response: result of the route that was originally called
        """
        api_token = request.headers.get("APP_API_TOKEN")

        if not api_token or api_token != app_settings.app_api_token:
            return JSONResponse({"error": "App Token missing or wrong"}, HTTPStatus.UNAUTHORIZED)

        response = await call_next(request)
        return response

    return app

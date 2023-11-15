from dotenv import dotenv_values

from app import create_app, app_settings

if __name__ == "__main__":
    import uvicorn

    config = dotenv_values(".env")
    uvicorn.run(create_app(), host=app_settings.app_host, port=app_settings.app_port)

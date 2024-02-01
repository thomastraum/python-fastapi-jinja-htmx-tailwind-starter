import os

from pathlib import Path
from typing import Any

from fastapi.responses import HTMLResponse
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Any

from dotenv import load_dotenv

load_dotenv()

APP_DIR = Path(__file__).resolve().parent

class Settings(BaseSettings):

    HOST: str
    PORT: int
    ENV: str 

    APP_DIR: Path = APP_DIR
    STATIC_DIR: Path = APP_DIR / 'static'
    TEMPLATE_DIR: Path = APP_DIR / 'templates'
    RENDER_DIR: Path = APP_DIR / 'static' / 'renders'
    UPLOAD_DIR: Path = APP_DIR / 'static' / 'uploads'

    FASTAPI_PROPERTIES: dict[str, Any] = {
        "title": "wss.renderer.ai",
        "description": "websockets htmx test, ui playgrounds",
        "version": "0.0.1",
        "default_response_class": HTMLResponse,  # Change default from JSONResponse
    }

    DISABLE_DOCS: bool = False

    @property
    def is_production(self):
        return self.ENV == "production"
    
    @property
    def is_development(self):
        return self.ENV == "development"

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        """Creates dictionary of values to pass to FastAPI app
        as **kwargs.

        Returns:
            dict: This can be unpacked as **kwargs to pass to FastAPI app.
        """
        fastapi_kwargs = self.FASTAPI_PROPERTIES
        if self.DISABLE_DOCS:
            fastapi_kwargs.update(
                {
                    "openapi_url": None,
                    "openapi_prefix": None,
                    "docs_url": None,
                    "redoc_url": None,
                }
            )
        return fastapi_kwargs

    def pretty_print(self):
        """Prints the settings in a human-readable format."""
        print("Settings:")
        for name, value in self:
            print(f"  {name}: {value}")

settings = Settings()
settings.pretty_print()





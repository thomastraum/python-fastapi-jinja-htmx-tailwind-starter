
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.config import settings, Settings
from app.routes import router, templates

from app.middleware import setup_exceptions, setup_browser_hotreload


class App:
    def __init__(self, settings: Settings):
        
        self.settings = settings
        self.app = FastAPI(**settings.fastapi_kwargs)
        self.app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")
        self.app.include_router(router)
        if settings.ENV == "development":
            setup_exceptions(self.app, templates)
            setup_browser_hotreload(self.app, templates)

app = App(settings=settings).app


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app", 
        host=settings.HOST, 
        port=settings.PORT,
        reload=settings.ENV == "development",
        reload_excludes=["./app/static/*"]
    )

    
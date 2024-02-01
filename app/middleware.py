from fastapi import FastAPI, Request

import arel
from jinja2_fragments.fastapi import Jinja2Blocks


def setup_browser_hotreload(app: FastAPI, templates: Jinja2Blocks):
    hot_reload = arel.HotReload(
        paths=[
            arel.Path("./app/templates/"),
            arel.Path("./app/static/css/"),
            # arel.Path("./*.py"),
        ]
    )
    app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    # print(Settings.is_development)
    templates.env.globals["DEBUG"] = True
    templates.env.globals["hot_reload"] = hot_reload


def setup_exceptions(app: FastAPI, templates: Jinja2Blocks):
    @app.exception_handler(Exception)
    async def unicorn_exception_handler(request: Request, exc: Exception):
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error_message": str(exc)},
            status_code=500,
        )

    return ""
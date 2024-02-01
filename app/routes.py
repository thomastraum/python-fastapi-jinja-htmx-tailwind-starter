
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from jinja2_fragments.fastapi import Jinja2Blocks

from app.config import settings

templates = Jinja2Blocks(directory=settings.TEMPLATE_DIR)  # Jinja2Blocks
templates.env.auto_reload = True

router = APIRouter()


@router.get("/")
async def index(request: Request):

    return templates.TemplateResponse(
        "main.html",
        {
            "request": request,
            "page_title": "hello! ",
            "errors": {},
        },
    )
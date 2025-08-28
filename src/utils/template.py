from fastapi.templating import Jinja2Templates

from src.config import settings

template = Jinja2Templates(directory=settings.templates.templates_path)
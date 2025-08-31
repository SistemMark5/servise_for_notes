import uvicorn
from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.utils.template import template
from src.views import router as notes_routers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # или ["*"] для всех источников
    allow_credentials=True,     # если используете куки
    allow_methods=["*"],        # GET, POST, PUT, DELETE и т.д.
    allow_headers=["*"],        # любые заголовки
)

app.mount("/static", StaticFiles(directory=settings.templates.static_path), name="static")
app.include_router(notes_routers)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
    # uvicorn.run("main:app", reload=True)

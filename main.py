import uvicorn
from fastapi import FastAPI
from src.views import router as notes_routers

app = FastAPI()

app.include_router(notes_routers)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

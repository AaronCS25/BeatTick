from fastapi import FastAPI
from .database import create_db_and_tables
from app.features.items.router import router as items_router
from contextlib import asynccontextmanager

app = FastAPI()

app.include_router(items_router, tags=["items"], prefix="/api")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    create_db_and_tables()
    yield
    # Shutdown
    pass

app = FastAPI(lifespan=lifespan)
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Server is up and running"}
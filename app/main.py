from fastapi import FastAPI
from .core.database import engine, Base
from app.features.tickets.routes import router as tickets_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="BeatTick")

app.include_router(tickets_router, prefix="/tickets", tags=["tickets"])

@app.get("/")
def read_root():
    return {"message": "Welcome to BeatTick"}
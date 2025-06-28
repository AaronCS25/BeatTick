from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from app.database import engine
from . import services
from .models import Item
from .schemas import ItemCreate

router = APIRouter()

def get_db():
    with Session(engine) as session:
        yield session

@router.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return services.create_item(db=db, item=item)

@router.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_items(db=db, skip=skip, limit=limit)
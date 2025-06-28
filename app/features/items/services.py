from sqlmodel import Session, select
from .models import Item
from .schemas import ItemCreate, ItemUpdate

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.exec(select(Item).offset(skip).limit(limit)).all()

def create_item(db: Session, item: ItemCreate):
    db_item = Item.model_validate(item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
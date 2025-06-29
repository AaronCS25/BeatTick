from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

class TicketRepository:
    def get_ticket(self, db: Session, ticket_id: int):
        return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

    def get_tickets_by_event(self, db: Session, event_id: int, skip: int = 0, limit: int = 100):
        return db.query(models.Ticket).filter(models.Ticket.event_id == event_id).offset(skip).limit(limit).all()

    def create_ticket(self, db: Session, ticket: schemas.TicketCreate, qr_code: str):
        db_ticket = models.Ticket(**ticket.model_dump(), qr_code=qr_code)
        db.add(db_ticket)
        db.commit()
        db.refresh(db_ticket)
        return db_ticket

    def validate_ticket(self, db: Session, qr_code: str):
        db_ticket = db.query(models.Ticket).filter(models.Ticket.qr_code == qr_code).first()
        if db_ticket and not db_ticket.used:
            db_ticket.used = True
            db_ticket.used_at = func.now()
            db.commit()
            db.refresh(db_ticket)
            return db_ticket
        return None
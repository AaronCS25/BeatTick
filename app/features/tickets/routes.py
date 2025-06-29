from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from . import schemas, services, repository

router = APIRouter()

ticket_repo = repository.TicketRepository()
ticket_service = services.TicketService(ticket_repo)

@router.post("/generate", response_model=schemas.Ticket)
def generate_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return ticket_service.generate_ticket(db, ticket)

@router.post("/validate")
def validate_ticket(ticket: schemas.TicketValidate, db: Session = Depends(get_db)):
    validated_ticket = ticket_service.validate_ticket(db, ticket.qr_code)
    if not validated_ticket:
        raise HTTPException(status_code=400, detail="Invalid or already used ticket")
    return {"message": "Ticket validated successfully"}

@router.get("/{ticket_id}", response_model=schemas.Ticket)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = ticket_service.get_ticket(db, ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.get("/event/{event_id}", response_model=List[schemas.Ticket])
def get_event_tickets(event_id: int, db: Session = Depends(get_db)):
    return ticket_service.get_event_tickets(db, event_id)
import qrcode
import uuid
from sqlalchemy.orm import Session
from . import schemas, repository

class TicketService:
    def __init__(self, repo: repository.TicketRepository):
        self.repo = repo

    def generate_ticket(self, db: Session, ticket: schemas.TicketCreate):
        qr_code_data = str(uuid.uuid4())
        # In a real application, you would save the QR code image and return a URL
        # For simplicity, we'll just return the QR data for now
        return self.repo.create_ticket(db, ticket, qr_code_data)

    def validate_ticket(self, db: Session, qr_code: str):
        return self.repo.validate_ticket(db, qr_code)

    def get_ticket(self, db: Session, ticket_id: int):
        return self.repo.get_ticket(db, ticket_id)

    def get_event_tickets(self, db: Session, event_id: int):
        return self.repo.get_tickets_by_event(db, event_id)
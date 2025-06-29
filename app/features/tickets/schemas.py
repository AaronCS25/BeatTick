from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TicketBase(BaseModel):
    user_id: int
    event_id: int

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int
    qr_code: str
    used: bool
    created_at: datetime
    used_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class TicketValidate(BaseModel):
    qr_code: str
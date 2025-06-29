from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    event_id = Column(Integer, index=True)
    qr_code = Column(String, unique=True, index=True)
    used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    used_at = Column(DateTime, nullable=True)
import uuid

from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ...database.connection import Base


class Store(Base):
    __tablename__ = 'stores'
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    location = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    time_updated = Column(DateTime(timezone=True), onupdate=func.now(), index=True)
    
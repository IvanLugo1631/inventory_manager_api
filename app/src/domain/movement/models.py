import uuid
from enum import Enum

from sqlalchemy import Column, DateTime, ForeignKey, String, Integer, Enum as SqlEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ...database.connection import Base


class MovementType(Enum):
    IN = "in"
    OUT = "out"
    TRANSFER = "transfer"

class Movement(Base):
    __tablename__ = 'movements'
    
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    product_id = Column(String, ForeignKey('products.id'), index=True, nullable=False)
    source_store_id = Column(String, ForeignKey('stores.id'), index=True, nullable=True)
    target_store_id = Column(String, ForeignKey('stores.id'), index=True, nullable=True)
    quantity = Column(Integer, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    time_updated = Column(DateTime(timezone=True), onupdate=func.now(), index=True)
    type = Column(SqlEnum(MovementType), nullable=False)
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ...database.connection import Base

class Inventory(Base):
    __tablename__ = 'inventory'
    
    id  = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    product_id = Column(String, ForeignKey('products.id'), index=True)
    store_id = Column(String, ForeignKey('stores.id'), index=True)
    category = Column(String, index=True)
    quantity = Column(Integer)
    min_stock = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    time_updated = Column(DateTime(timezone=True), onupdate=func.now(), index=True)
    
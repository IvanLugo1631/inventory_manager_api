from sqlalchemy import Column, DateTime, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database.connection import Base

class Inventory(Base):
    __tablename__ = 'inventory'
    
    id  = Column(String, primary_key=True, index=True)
    product_id = Column(String, ForeignKey('products.id'), index=True)
    description = Column(String)
    category = Column(String, index=True)
    price = Column(Float)
    sku = Column(String, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    time_updated = Column(DateTime(timezone=True), onupdate=func.now(), index=True)
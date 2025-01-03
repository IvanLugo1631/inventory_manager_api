from sqlalchemy import Column, DateTime, String, Float
from sqlalchemy.sql import func
from ...database.connection import Base

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    category = Column(String, index=True)
    price = Column(Float)
    sku = Column(String, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    time_updated = Column(DateTime(timezone=True), onupdate=func.now(), index=True)
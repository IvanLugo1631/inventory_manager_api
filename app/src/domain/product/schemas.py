# schemas.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    """Base schema shared across various operations.
    """
    
    name: str
    description: str
    category: str
    price: float
    sku: str
    
    model_config = ConfigDict(from_attributes=True)

class ProductCreate(ProductBase):
    """Schema for creating a new product.
    """
     
    pass

class ProductUpdate(BaseModel):
    """Schema for updating a product (partial updates allowed).
    """
    
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    sku: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)

class Product(ProductBase):
    """Schema for representing a product with additional fields.
    """
    
    id: str
    time_created: datetime
    time_updated: Optional[datetime] = None
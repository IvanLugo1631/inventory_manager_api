from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class InventoryBase(BaseModel):
    """Base schema shared across various operations.
    """
    
    product_id: str
    store_id: str
    quantity: int
    min_stock: int
    category: str
    
    model_config = ConfigDict(from_attributes=True)
    
class InventoryCreate(InventoryBase):
    """Schema for creating a new inventory item.
    """
    
    pass

class InventoryUpdate(BaseModel):
    """Schema for updating an inventory item (partial updates allowed).
    """
    
    product_id: Optional[str] = None
    store_id: Optional[str] = None
    quantity: Optional[int] = None
    min_stock: Optional[int] = None
    category: Optional[str] = None
        
    model_config = ConfigDict(from_attributes=True)
    
class Inventory(InventoryBase):
    """Schema for representing an inventory item with additional fields.
    """
    
    id: str
    time_created: datetime
    time_updated: Optional[datetime] = None

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class MovementBase(BaseModel):
    """Base schema shared across various operations.
    """
    
    product_id: str
    quantity: int
    type: str
    
    model_config = ConfigDict(from_attributes=True)

class MovementCreate(MovementBase):
    """Schema for creating a new movement record.
    """
    
    source_store_id: str
    target_store_id: str
    
class Movement(MovementBase):
    """Schema for representing a movement record with additional fields.
    """
    
    id: str
    time_created: datetime
    time_updated: Optional[datetime] = None

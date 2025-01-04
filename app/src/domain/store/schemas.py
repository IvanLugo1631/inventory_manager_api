from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class StoreBase(BaseModel):
    """Schema for creating a new store.
    """
    #     id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    # name = Column(String, index=True)
    # location = Column(String)
    # time_created = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    # time_updated = Column(DateTime(timezone=True), onupdate=func.now(), index=True)

    name: str
    location: str
    
    model_config = ConfigDict(from_attributes=True)

class StoreCreate(StoreBase):
    """Schema for creating a new store.
    """
    pass

class StoreUpdate(StoreBase):
    """Schema for updating a store.
    """
    name: Optional[str]
    location: Optional[str]
    
    model_config = ConfigDict(from_attributes=True)

class Store(StoreBase):
    """Schema for a store.
    """
    id: str
    time_created: datetime
    time_updated: Optional[datetime] = None
        
    model_config = ConfigDict(from_attributes=True)

    
# services.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import models, schemas
from fastapi import HTTPException

def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    """Create a new inventory record.
    """
    
    db_inventory = models.Inventory(**inventory.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def get_inventory(db: Session, inventory_id: str):
    """Get a single inventory record by ID.
    """
    
    return db.query(models.Inventory).filter_by(id=inventory_id).first()

def get_inventory_records(db: Session, skip: int = 0, limit: int = 100):
    """Get all inventory records with pagination.
    """
    
    return db.query(models.Inventory).offset(skip).limit(limit).all()

def inventory_update(db: Session, inventory_id: str, inventory: schemas.InventoryUpdate):
    """Update an inventory record.
    """
    
    db_inventory = db.query(models.Inventory).filter_by(id=inventory_id).first()
    if not db_inventory:
        raise HTTPException(status_code=404, detail="Inventory record not found.")
    
    for key, value in inventory.dict(exclude_unset=True).items():
        setattr(db_inventory, key, value)
    
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def delete_inventory(db: Session, inventory_id: str):
    """Delete an inventory record.
    """
    
    db_inventory = db.query(models.Inventory).filter_by(id=inventory_id).first()
    if not db_inventory:
        raise HTTPException(status_code=404, detail="Inventory record not found.")
    
    db.delete(db_inventory)
    db.commit()
    return db_inventory

def get_inventory_by_store(db: Session, store_id: str):
    """Retrieve inventory items for a specific store.
    """
    
    return db.query(models.Inventory).filter_by(store_id=store_id).all()


def get_inventory_alerts(db: Session):
    """Retrieve inventory items below minimum stock.
    """
    
    return db.query(models.Inventory).filter(models.Inventory.quantity < models.Inventory.min_stock).all()
from typing import List, Optional
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def create_store(db: Session, store: schemas.StoreCreate) -> models.Store:
    """Create a new store.
    """
    print(store)
    try:
        db_store = models.Store(**store.dict())
        db.add(db_store)
        db.commit()
        db.refresh(db_store)
        return db_store
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
def get_store(db: Session, store_id: str) -> Optional[models.Store]:
    """Retrieve a store by ID.
    """
    
    store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

def get_stores(db: Session, skip: int = 0, limit: int = 100) -> List[models.Store]:
    """Retrieve multiple stores.
    """
    
    return db.query(models.Store).offset(skip).limit(limit).all()

def update_store(db: Session, store_id: str, store: schemas.StoreUpdate) -> models.Store:
    """Update a store by ID.
    """
    
    db_store = get_store(db, store_id)
    
    try:
        update_data = store.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_store, field, value)
        db.commit()
        db.refresh(db_store)
        return db_store
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
def delete_store(db: Session, store_id: str) -> models.Store:
    """Delete a store by ID.
    """
    
    db_store = get_store(db, store_id)
    
    try:
        db.delete(db_store)
        db.commit()
        return db_store
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

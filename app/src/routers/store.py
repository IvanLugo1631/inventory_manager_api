from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.src.routers import dependencies
from app.src.domain.store import schemas, services

router = APIRouter(
    prefix="/api/stores",
    tags=["stores"]
)

@router.post("/", response_model=schemas.Store)
def create_store(store: schemas.StoreCreate, db: Session = Depends(dependencies.get_db)):
    """Create a new store.
    """
    print(store)
    return services.create_store(db=db, store=store)

@router.get("/{store_id}", response_model=schemas.Store)
def get_store(store_id: str, db: Session = Depends(dependencies.get_db)):
    """Get a single store by ID.
    """
    return services.get_store(db=db, store_id=store_id)

@router.get("/", response_model=List[schemas.Store])
def get_stores(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    """Get all stores with pagination.
    """
    return services.get_stores(db=db, skip=skip, limit=limit)

@router.patch("/{store_id}", response_model=schemas.Store)
def update_store(store_id: str, store: schemas.StoreUpdate, db: Session = Depends(dependencies.get_db)):
    """Update a store.
    """
    return services.update_store(db=db, store_id=store_id, store=store)

@router.delete("/{store_id}", response_model=schemas.Store)
def delete_store(store_id: str, db: Session = Depends(dependencies.get_db)):
    """Delete a store.
    """
    return services.delete_store(db=db, store_id=store_id)
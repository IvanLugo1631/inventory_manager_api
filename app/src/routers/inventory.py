from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from app.src.routers import dependencies
from app.src.domain.inventory import schemas as schemasInventory
from app.src.domain.movement import schemas as schemasMovement
from app.src.domain.inventory import services as inventoryServices
from app.src.domain.movement import services as movementServices

router = APIRouter(
    prefix="/api/inventory",
    tags=["inventory"]
)

@router.post("/", response_model=schemasInventory.Inventory)
def create_inventory(
    inventory: schemasInventory.InventoryCreate, 
    db: Session = Depends(dependencies.get_db)
):
    """Create a new inventory record."""
    try:
        return inventoryServices.create_inventory(db=db, inventory=inventory)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/{inventory_id}", response_model=schemasInventory.Inventory)
def get_inventory(
    inventory_id: str, 
    db: Session = Depends(dependencies.get_db)
):
    """Get a single inventory record by ID."""
    try:
        inventory = inventoryServices.get_inventory(db=db, inventory_id=inventory_id)
        if not inventory:
            raise HTTPException(status_code=404, detail="Inventory record not found")
        return inventory
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/", response_model=List[schemasInventory.Inventory])
def get_inventory_records(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(dependencies.get_db)
):
    """Get all inventory records with pagination."""
    try:
        return inventoryServices.get_inventory_records(db=db, skip=skip, limit=limit)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.patch("/{inventory_id}", response_model=schemasInventory.Inventory)
def update_inventory(
    inventory_id: str, 
    inventory: schemasInventory.InventoryUpdate, 
    db: Session = Depends(dependencies.get_db)
):
    """Update an inventory record."""
    try:
        return inventoryServices.inventory_update(db=db, inventory_id=inventory_id, inventory=inventory)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.delete("/{inventory_id}", response_model=schemasInventory.Inventory)
def delete_inventory(
    inventory_id: str, 
    db: Session = Depends(dependencies.get_db)
):
    """Delete an inventory record."""
    try:
        return inventoryServices.delete_inventory(db=db, inventory_id=inventory_id)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/store/{store_id}", response_model=List[schemasInventory.Inventory])
def get_inventory_by_store(
    store_id: str, 
    db: Session = Depends(dependencies.get_db)
):
    """Retrieve inventory items for a specific store."""
    try:
        return inventoryServices.get_inventory_by_store(db=db, store_id=store_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/transfer", response_model=schemasMovement.Movement)
def transfer_inventory(
    movement: schemasMovement.MovementCreate, 
    db: Session = Depends(dependencies.get_db)
):
    """Transfer products between stores."""
    try:
        return movementServices.transfer_inventory(db=db, movement=movement)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/alerts", response_model=List[schemasInventory.Inventory])
def get_inventory_alerts(db: Session = Depends(dependencies.get_db)):
    """Retrieve inventory items below minimum stock."""
    try:
        return services.get_inventory_alerts(db=db)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

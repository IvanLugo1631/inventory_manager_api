from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import models, schemas
from ..inventory import models as modelsInventory
from fastapi import HTTPException


def transfer_inventory(db: Session, movement: schemas.MovementCreate):
    """Transfer products between stores."""
    try:
        source_inventory = (
            db.query(modelsInventory.Inventory)
            .filter_by(store_id=movement.source_store_id, product_id=movement.product_id)
            .first()
        )
        if not source_inventory or source_inventory.quantity < movement.quantity:
            raise HTTPException(status_code=400, detail="Insufficient stock at source.")

        target_inventory = (
            db.query(modelsInventory.Inventory)
            .filter_by(store_id=movement.target_store_id, product_id=movement.product_id)
            .first()
        )
        if not target_inventory:
            target_inventory = modelsInventory.Inventory(
                store_id=movement.target_store_id,
                product_id=movement.product_id,
                quantity=0,
                min_stock=source_inventory.min_stock,
                category=source_inventory.category,
            )
            db.add(target_inventory)

        # Update source and target inventory
        source_inventory.quantity -= movement.quantity
        target_inventory.quantity += movement.quantity

        # Log the movement
        db_movement = models.Movement(**movement.model_dump())
        db.add(db_movement)
        db.commit()

        return db_movement
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

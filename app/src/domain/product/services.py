# services.py
from typing import List, Optional
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def create_product(db: Session, product: schemas.ProductCreate) -> models.Product:
    """Create a new product.
    """
    
    try:
        db_product = models.Product(**product.model_dump())  #model_dump() is a method that returns a dictionary of the model
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def get_product(db: Session, product_id: str) -> Optional[models.Product]:
    """Retrieve a product by ID.
    """
    
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def get_products(db: Session, skip: int = 0, limit: int = 100) -> List[models.Product]:
    """Retrieve multiple products.
    """
    
    return db.query(models.Product).offset(skip).limit(limit).all()

def update_product(db: Session, product_id: str, product: schemas.ProductUpdate) -> models.Product:
    """Update a product by ID.
    """
    
    db_product = get_product(db, product_id)
    
    try:
        update_data = product.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_product, field, value)
        db.commit()
        db.refresh(db_product)
        return db_product
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def delete_product(db: Session, product_id: str) -> models.Product:
    """Delete a product by ID.
    """
    
    db_product = get_product(db, product_id)
    
    try:
        db.delete(db_product)
        db.commit()
        return db_product
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
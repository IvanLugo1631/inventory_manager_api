# app/src/routers/product.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.src.routers import dependencies
from app.src.domain.product import schemas, services

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(dependencies.get_db)):
    """Create a new product.
    """
    return services.create_product(db=db, product=product)

@router.get("/{product_id}", response_model=schemas.Product)
def get_product(product_id: str, db: Session = Depends(dependencies.get_db)):
    """Get a single product by ID."""
    return services.get_product(db=db, product_id=product_id)

@router.get("/", response_model=List[schemas.Product])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    """Get all products with pagination."""
    return services.get_products(db=db, skip=skip, limit=limit)

@router.patch("/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: str, 
    product: schemas.ProductUpdate, 
    db: Session = Depends(dependencies.get_db)
):
    """Update a product.
    """
    return services.update_product(db=db, product_id=product_id, product=product)

@router.delete("/{product_id}", response_model=schemas.Product)
def delete_product(product_id: str, db: Session = Depends(dependencies.get_db)):
    """Delete a product.
    """
    return services.delete_product(db=db, product_id=product_id)
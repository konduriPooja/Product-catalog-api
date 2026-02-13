from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


# READ ALL
@router.get("/", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


#READ ONE
@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


#UPDATE
@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    existing_product = db.query(models.Product).filter(models.Product.id == product_id).first()

    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.in_stock = product.in_stock

    db.commit()
    db.refresh(existing_product)
    return existing_product


#DELETE
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}

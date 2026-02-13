from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool = True

class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True

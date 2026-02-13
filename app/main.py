from fastapi import FastAPI
from app.database import engine, Base
from app.models import Product
from app.routes.product_routes import router as product_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Catalog API")

app.include_router(product_router)


@app.get("/")
def root():
    return {"message": "Product Catalog API is running"}

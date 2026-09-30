"""
Capstone: Products REST API

Ties together: FastAPI, OOP, dataclasses, type hints,
exceptions, logging, and environment config.
"""
import logging
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import models
from config import APP_TITLE

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title=APP_TITLE)


class ProductIn(BaseModel):
    name: str
    price: float
    in_stock: bool = True

class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


@app.get("/products", response_model=List[ProductOut])
def list_products():
    return models.all_products()

@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int):
    product = models.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=ProductOut, status_code=201)
def create_product(data: ProductIn):
    product = models.create_product(data.name, data.price, data.in_stock)
    logger.info("Created product id=%s name=%s", product.id, product.name)
    return product

@app.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: int, data: ProductIn):
    product = models.update_product(product_id, data.name, data.price, data.in_stock)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    if not models.delete_product(product_id):
        raise HTTPException(status_code=404, detail="Product not found")


if __name__ == "__main__":
    import uvicorn
    from config import PORT
    uvicorn.run(app, host="0.0.0.0", port=PORT)

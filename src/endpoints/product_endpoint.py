from typing import List

from fastapi import APIRouter
from src.services.product_service import ProductService

from src.config.bdd_config import db_dependency
from src.schemas.product_schema import ProductCreate

product_router = APIRouter(prefix="/products", tags=["products"])
@product_router.get("/")
async def get_products(db:db_dependency):
    return ProductService.get_products(db)

@product_router.get("/{product_id}")
async def get_product_by_id(db:db_dependency, product_id:int):
    return ProductService.get_product_by_id(db,product_id)
@product_router.post("/")
async def create_product(db:db_dependency,product:ProductCreate):
    return ProductService.createProduct(db,product)

@product_router.post("/list")
async def create_product(db:db_dependency, products: List[ProductCreate]):
    return ProductService.create_products(db,products)


@product_router.put("/{product_id}")
async def update_product(db:db_dependency,product_id:int,product:ProductCreate):
    return ProductService.edit_product(db,product_id,product)


@product_router.delete("/{product_id}")
async def delete_product(db:db_dependency,product_id:int):
    return ProductService.delete_product(db,product_id)
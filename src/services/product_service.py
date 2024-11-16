from typing import List

from poetry.repositories import Repository

from src.repositories.productrepository import ProductRepository
from src.schemas.product_schema import ProductBase, ProductCreate

class ProductService:
    def __init__(self):
        pass

    @classmethod
    def createProduct(self,db, product:ProductBase):
        return ProductRepository.create_product(db, product)

    @classmethod
    def create_products(self,db, products:List[ProductBase]):
        return ProductRepository.create_products(db, products)

    @classmethod
    def edit_product(self,db,product_id:int,product:ProductCreate):
        return ProductRepository.edit_product(db, product_id, product)

    @classmethod
    def get_products(self,db):
        return ProductRepository.get_products(db)

    @classmethod
    def delete_product(self,db,product_id:int):
        return ProductRepository.delete_product(db, product_id)

    @classmethod
    def get_product_by_id(self,db,product_id:int):
        return ProductRepository.get_product_by_id(db, product_id)

    @classmethod
    def stock_availble(self,db,qty:int,product_id:int):
        data_product = ProductRepository.get_stock_by_id(db,product_id)
        if data_product['stock'] >= qty :
            return True
        else :
            return False

    @classmethod
    def update_stock_for_product(self, db, quantité, produit_id):
        ProductRepository.update_stock_for_product (db,quantité,produit_id)
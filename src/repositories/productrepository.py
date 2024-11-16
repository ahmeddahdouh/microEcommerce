from fastapi import HTTPException
from starlette import status
from src.models.product_model import Product
from src.schemas.product_schema import ProductBase, ProductResponse, ProductCreate
from sqlalchemy.orm import Session

class ProductRepository:
    def __init__(self):
        pass

    def create_product(db:Session,product : ProductBase)  -> ProductResponse:
        product_db = Product(name=product.nom, description=product.description, price=product.prix,stock = product.stock)
        db.add(product_db)
        db.commit()
        db.refresh(product_db)
        return product_db

    def edit_product(db: Session, product_id, product:ProductCreate) -> ProductCreate:
        db_product = db.query(Product).filter(Product.id == product_id).first()

        if not db_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Produit avec ID {product_id} introuvable."
            )

        db_product.name = product.nom
        db_product.description = product.description
        db_product.price = product.prix
        db_product.stock = product.stock

        db.commit()
        db.refresh(db_product)

        return product

    def get_products(db):
        return db.query(Product).all()

    def delete_product(db: Session, product_id: int):
        product_to_delete = db.query(Product).filter(Product.id == product_id).first()

        if not product_to_delete:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Produit avec ID {product_id} introuvable.")
        else:
            db.delete(product_to_delete)
            db.commit()  # Commit pour supprimer le produit de la base de données

        return {"message": "Produit supprimé avec succès"}

    def get_product_by_id(db,product_id:int):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product :
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Produit avec ID {product_id} introuvable."
            )
        else:
            return db_product

    @classmethod
    def create_products(self,db, products):
        for product in products:
            self.create_product(db,product)
        return {"message": "Liste de produits créée avec succès"}






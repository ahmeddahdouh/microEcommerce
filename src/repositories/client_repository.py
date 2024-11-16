from fastapi import HTTPException

from starlette import status

from src.models.client_model import Client
from src.schemas.client_schema import ClientBase


class ClientRepository:
    def __init__(self):
        pass

    def create_client(db,client:ClientBase):
        client_db = Client(nom = client.nom,email = client.email)
        db.add(client_db)
        db.commit()
        db.refresh(client_db)
        return client_db

    def get_client_by_id(db, client_id):
        client_db = db.query(Client).filter(Client.id == client_id).first()
        if not client_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,  # Spécifier le code de statut HTTP
                detail=f"Produit avec ID {client_id} introuvable."  # Message d'erreur
            )
        else :
            return client_db

    def get_clients(db):
        return db.query(Client).all()

    @classmethod
    def delete_client(self,db, client_id):
        client_to_delete = self.get_client_by_id(db, client_id)
        db.delete(client_to_delete)
        db.commit()
        return {"message":"Client deleted"}

    @classmethod
    def update_client(cls, db, client_id,client:ClientBase):
        client_db = db.query(Client).filter(Client.id == client_id).first()
        if not client_db:
            raise HTTPException("test")
        else :
            client_db.name = client.nom
            client_db.email = client.email
            db.commit()
        return client_db


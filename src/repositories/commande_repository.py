from datetime import datetime
from fastapi import HTTPException

from dns.e164 import query
from sqlalchemy.orm import Session

from src.models import Commande
from src.schemas.commande_schema import CommandeBase, CommandeUpdate


class CommandeRepository:
    def __init__(self):
        pass

    @classmethod
    def create(self,db:Session,commande:CommandeBase):
        commande_db = Commande(client_id = commande.client_id,
                               produit_id = commande.produit_id,
                               quantité = commande.quantité,
                               date_commande = datetime.now(),
                               etat_commande =commande.etat_commande)
        db.add(commande_db)
        db.commit()
        db.refresh(commande_db)
        return commande_db

    def get_commandes(db:Session):
        return db.query(Commande).all()


    def get_commande_by_id(db:Session,commande_id:int):
        commande_db = db.query(Commande).filter(Commande.id == commande_id).first()
        if not commande_db :
            raise HTTPException(status_code=404, detail="Item not found")
            return None
        else :
            return commande_db

    def get_commande_by_id(db,commande_id:int):
        db_commande = db.query(Commande).filter(Commande.id == commande_id).first()
        if not db_commande :
           raise HTTPException(status_code=404, detail="Item not found")
        else :
            return db_commande

    @classmethod
    def delete_commande(self,db:Session,commande_id:int):
        db_commande =  self.get_commande_by_id(db,commande_id)
        if db_commande:
            db.delete(db_commande)
            db.commit()
            return {'message':'order deleted successfully'}

    @classmethod
    def update_commande(self,db:Session,commande_id:int,commande : CommandeUpdate):
        db_commande = self.get_commande_by_id(db,commande_id)
        if db_commande :
            db_commande.client_id = commande.client_id
            db_commande.produit_id = commande.produit_id
            db_commande.quantité = commande.quantité
            db_commande.etat_commande = commande.etat_commande
            db.commit()
            db.refresh(db_commande)
            return db_commande

    @classmethod
    def update_status_commande(self,db:Session,commande_id:int,status:str):
        db_commande = self.get_commande_by_id(db,commande_id)
        if db_commande :
            db_commande.status = status
            db.commit()
            db.refresh(db_commande)
            return db_commande




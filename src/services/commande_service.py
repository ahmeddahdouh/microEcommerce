from lib2to3.fixer_util import Comma

from sqlalchemy.orm import Session

from src.repositories.commande_repository import CommandeRepository
from src.schemas.commande_schema import CommandeBase, CommandeUpdate


class CommandeService:
    def __init__(self):
        pass

    def create_commande(db,commande:CommandeBase):
        return CommandeRepository.create(db,commande)

    def get_commandes(db):
        return CommandeRepository.get_commandes(db)

    def get_commande_by_id(db,commande_id:int):
        return CommandeRepository.get_commande_by_id(db,commande_id)

    def update_commande(db, commande_id,commande:CommandeUpdate):
        return CommandeRepository.update_commande(db,commande_id,commande)

    def delete_commande(db:Session,commande_id):
        return CommandeRepository.delete_commande(db,commande_id)

    @classmethod
    def update_commande_status(self, db, commande_id, status):
        return CommandeRepository.update_status_commande(db,commande_id,status)


from sys import prefix

from fastapi import APIRouter

from src.config.bdd_config import db_dependency
from src.schemas.commande_schema import CommandeBase, CommandeUpdate
from src.services.commande_service import CommandeService

commande_router = APIRouter(prefix="/commande", tags=["commande"])

@commande_router.get("/")
async def list_commandes(db:db_dependency):
    return CommandeService.get_commandes(db)

@commande_router.get("/{id_commande}")
async def get_commande(db:db_dependency,id_commande:int):
    return CommandeService.get_commande_by_id(db,id_commande)
@commande_router.post("/")
async def create_commande(db:db_dependency,commande: CommandeBase):
    return CommandeService.create_commande(db,commande)

@commande_router.delete("/")
async def delete_commande(db:db_dependency,commande_id : int):
    return CommandeService.delete_commande(db,commande_id)

@commande_router.put("/{id_commande}")
async def update_commande(db:db_dependency , commande_id : int , commande : CommandeUpdate):
    return  CommandeService.update_commande(db,commande_id,commande)

@commande_router.put("/{id_commande}/{status}")
async def update_commande(db:db_dependency , commande_id : int , status : str):
    return CommandeService.update_commande_status(db,commande_id,status)





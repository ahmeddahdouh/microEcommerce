from fastapi import APIRouter
from src.config.bdd_config import db_dependency
from src.schemas.client_schema import ClientBase
from src.services.client_service import ClientService

client_router= APIRouter(prefix='/clients',tags=['client'])


@client_router.post('/')
async def create_client(db:db_dependency,client:ClientBase):
    return ClientService.create_client(db,client)

@client_router.get('/')
async def list_clients(db:db_dependency):
    return ClientService.get_clients(db)

@client_router.get('/{client_id}')
async def get_client(db:db_dependency,client_id:str):
    return ClientService.get_client_by_id(db,client_id)

@client_router.delete('/{client_id}')
async def delete_client(db:db_dependency,client_id:str):
    return ClientService.delete_client(db,client_id)

@client_router.put('/{client_id}')
async def update_client(db:db_dependency,client_id:str,client:ClientBase):
    return ClientService.update_client(db,client_id,client)


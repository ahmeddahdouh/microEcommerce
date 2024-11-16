from src.repositories.client_repository import ClientRepository
from src.schemas.client_schema import ClientBase


class ClientService:

    def __init__(self):
        pass

    def create_client(db,client):
        return ClientRepository.create_client(db,client)

    def get_clients(db):
        return ClientRepository.get_clients(db)

    def get_client_by_id(db,client_id):
        return ClientRepository.get_client_by_id(db, client_id)

    def delete_client(db,client_id):
        return ClientRepository.delete_client(db,client_id)

    @classmethod
    def update_client(self, db, client_id,client: ClientBase):
        return ClientRepository.update_client(db,client_id,client)
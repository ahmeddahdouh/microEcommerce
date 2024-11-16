from pydantic import BaseModel, EmailStr


class ClientBase(BaseModel):
    nom : str
    email : EmailStr

class ClientCreate(ClientBase):
    pass

class ClientResponse(ClientBase):
    id:int
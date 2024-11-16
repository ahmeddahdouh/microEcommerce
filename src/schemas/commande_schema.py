from datetime import date

from pydantic import BaseModel

class CommandeBase(BaseModel):
    client_id: int
    produit_id: int
    quantité: int
    date_commande: date
    etat_commande: str

    class Config:
        orm_mode = True
class CommandeUpdate(BaseModel):
    client_id: int
    produit_id: int
    quantité: int
    etat_commande: str

class CommandeResponse(CommandeBase):
    id: int



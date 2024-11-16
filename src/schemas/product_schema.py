from pydantic import BaseModel


class ProductBase(BaseModel):
    nom:str
    description:str
    prix:float
    stock:int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int


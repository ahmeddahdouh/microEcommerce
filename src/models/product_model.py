from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from src.config.bdd_config import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)



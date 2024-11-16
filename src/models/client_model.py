from sqlalchemy import Column, Integer, String

from src.config.bdd_config import Base


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String,nullable=False)
    email = Column(String, nullable=False)

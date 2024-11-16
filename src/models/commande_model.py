from sqlalchemy import Column, Integer, String, ForeignKey, Date

from src.config.bdd_config import Base


class Commande(Base):
    __tablename__ = 'commandes'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    produit_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantité = Column(Integer, nullable=False)
    date_commande = Column(Date, nullable=False)
    etat_commande = Column(String, nullable=False)
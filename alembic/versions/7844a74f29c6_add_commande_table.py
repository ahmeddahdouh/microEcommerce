"""add commande table

Revision ID: 7844a74f29c6
Revises: bc9a3bdc4e71
Create Date: 2024-11-09 08:59:05.378296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7844a74f29c6'
down_revision: Union[str, None] = 'bc9a3bdc4e71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('commandes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('produit_id', sa.Integer(), nullable=False),
    sa.Column('quantité', sa.Integer(), nullable=False),
    sa.Column('date_commande', sa.Date(), nullable=False),
    sa.Column('etat_commande', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['produit_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('commandes')
    # ### end Alembic commands ###

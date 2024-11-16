"""add client table to the database2

Revision ID: bc9a3bdc4e71
Revises: 8206759c4913
Create Date: 2024-11-09 08:20:40.580819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc9a3bdc4e71'
down_revision: Union[str, None] = '8206759c4913'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nom', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('client')
    # ### end Alembic commands ###

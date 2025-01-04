"""empty message

Revision ID: a314ef92c60f
Revises: f2f6753cd85a
Create Date: 2025-01-04 15:33:37.473450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a314ef92c60f'
down_revision: Union[str, None] = 'f2f6753cd85a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('product_id', sa.String(), nullable=True),
    sa.Column('store_id', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('min_stock', sa.Integer(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_category'), 'inventory', ['category'], unique=False)
    op.create_index(op.f('ix_inventory_id'), 'inventory', ['id'], unique=False)
    op.create_index(op.f('ix_inventory_product_id'), 'inventory', ['product_id'], unique=False)
    op.create_index(op.f('ix_inventory_store_id'), 'inventory', ['store_id'], unique=False)
    op.create_index(op.f('ix_inventory_time_created'), 'inventory', ['time_created'], unique=False)
    op.create_index(op.f('ix_inventory_time_updated'), 'inventory', ['time_updated'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_inventory_time_updated'), table_name='inventory')
    op.drop_index(op.f('ix_inventory_time_created'), table_name='inventory')
    op.drop_index(op.f('ix_inventory_store_id'), table_name='inventory')
    op.drop_index(op.f('ix_inventory_product_id'), table_name='inventory')
    op.drop_index(op.f('ix_inventory_id'), table_name='inventory')
    op.drop_index(op.f('ix_inventory_category'), table_name='inventory')
    op.drop_table('inventory')
    # ### end Alembic commands ###

"""adding_enum_type

Revision ID: 0ec0e50ca16f
Revises: a993d24a151d
Create Date: 2025-01-03 18:38:14.191382

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ec0e50ca16f'
down_revision: Union[str, None] = 'a993d24a151d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the enum type
    movement_type_enum = sa.Enum('IN', 'OUT', 'TRANSFER', name='movementtype')
    movement_type_enum.create(op.get_bind())

    # Add the column with the new enum type
    op.add_column('movements', sa.Column('type', movement_type_enum, nullable=False))

def downgrade() -> None:
    # Drop the column
    op.drop_column('movements', 'type')

    # Drop the enum type
    movement_type_enum = sa.Enum('IN', 'OUT', 'TRANSFER', name='movementtype')
    movement_type_enum.drop(op.get_bind())

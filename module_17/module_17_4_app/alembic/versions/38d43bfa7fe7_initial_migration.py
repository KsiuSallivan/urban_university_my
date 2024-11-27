"""Initial migration

Revision ID: 38d43bfa7fe7
Revises: 
Create Date: 2024-11-17 15:06:47.814389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38d43bfa7fe7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

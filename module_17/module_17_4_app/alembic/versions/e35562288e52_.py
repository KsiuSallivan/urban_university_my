"""empty message

Revision ID: e35562288e52
Revises: 7111bb0ed1ee
Create Date: 2024-11-21 15:21:22.952754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e35562288e52'
down_revision: Union[str, None] = '7111bb0ed1ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

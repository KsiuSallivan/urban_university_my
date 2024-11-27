"""empty message

Revision ID: 7111bb0ed1ee
Revises: be1e4fb9b5f1
Create Date: 2024-11-21 15:20:11.535509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7111bb0ed1ee'
down_revision: Union[str, None] = 'be1e4fb9b5f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

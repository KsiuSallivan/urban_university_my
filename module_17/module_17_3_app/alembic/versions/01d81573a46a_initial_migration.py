"""Initial migration

Revision ID: 01d81573a46a
Revises: 38d43bfa7fe7
Create Date: 2024-11-17 15:15:57.840905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '01d81573a46a'
down_revision: Union[str, None] = '38d43bfa7fe7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

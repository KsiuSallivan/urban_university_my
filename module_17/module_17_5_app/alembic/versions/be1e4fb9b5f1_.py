"""empty message

Revision ID: be1e4fb9b5f1
Revises: 01d81573a46a
Create Date: 2024-11-21 14:09:52.694345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be1e4fb9b5f1'
down_revision: Union[str, None] = '01d81573a46a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

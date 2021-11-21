"""adds_list_item_statuses

Revision ID: b7bcdc6bfcc6
Revises: ea23779cf0d4
Create Date: 2021-11-21 19:52:10.380130+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from src.migrations.seed.seed_list_item_statuses import seed_list_item_statuses

revision = 'b7bcdc6bfcc6'
down_revision = 'ea23779cf0d4'
branch_labels = None
depends_on = None


def upgrade():
    seed_list_item_statuses()


def downgrade():
    pass

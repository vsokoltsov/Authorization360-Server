"""users_salt

Revision ID: 8315590101cc
Revises: ed974e27d968
Create Date: 2019-04-28 08:03:00.020088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8315590101cc'
down_revision = 'ed974e27d968'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('salt', sa.Text, nullable=True),)


def downgrade():
    op.drop_column('users', 'salt')

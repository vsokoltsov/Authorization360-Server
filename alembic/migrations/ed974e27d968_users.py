"""users

Revision ID: ed974e27d968
Revises: 
Create Date: 2019-04-27 21:40:16.750514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed974e27d968'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('first_name', sa.String(255), nullable=True),
        sa.Column('last_name', sa.String(255), nullable=True),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
    )
    op.create_index("unique_user_email", "users", ["email"], unique=True)


def downgrade():
    op.drop_index('unique_user_email', 'users')
    op.drop_table('users')

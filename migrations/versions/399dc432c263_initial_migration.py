"""Initial Migration

Revision ID: 399dc432c263
Revises: 
Create Date: 2023-11-17 14:52:10.190906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '399dc432c263'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mobs',
    sa.Column('mob_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('hit_points', sa.Integer(), nullable=False),
    sa.Column('damage', sa.Integer(), nullable=False),
    sa.Column('speed', sa.Integer(), nullable=False),
    sa.Column('is_hostile', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('mob_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mobs')
    # ### end Alembic commands ###
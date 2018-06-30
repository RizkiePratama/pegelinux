"""empty message

Revision ID: 07105363599f
Revises: 5d01d82188c8
Create Date: 2018-06-29 17:01:44.107616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07105363599f'
down_revision = '5d01d82188c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner', sa.String(length=120), nullable=True),
    sa.Column('rss', sa.String(length=128), nullable=True),
    sa.Column('html', sa.String(length=128), nullable=True),
    sa.Column('approved', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('html'),
    sa.UniqueConstraint('rss')
    )
    op.create_index(op.f('ix_feed_owner'), 'feed', ['owner'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_feed_owner'), table_name='feed')
    op.drop_table('feed')
    # ### end Alembic commands ###
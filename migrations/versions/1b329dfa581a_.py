"""empty message

Revision ID: 1b329dfa581a
Revises: 
Create Date: 2022-05-24 22:22:38.862440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b329dfa581a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('whiskey',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('brand', sa.String(length=200), nullable=True),
    sa.Column('size', sa.String(length=50), nullable=True),
    sa.Column('proof', sa.String(length=50), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('whiskey')
    op.drop_table('user')
    # ### end Alembic commands ###
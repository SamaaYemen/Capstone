"""empty message

Revision ID: 1fb321d1940c
Revises: 361be2e2f7d8
Create Date: 2020-07-04 20:22:10.091023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fb321d1940c'
down_revision = '361be2e2f7d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('industries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('industry', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_job', sa.Boolean(), nullable=True),
    sa.Column('profile_image', sa.String(length=500), nullable=True),
    sa.Column('industry_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['industry_id'], ['industries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('table')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('table',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='table_pkey')
    )
    op.drop_table('person')
    op.drop_table('industries')
    # ### end Alembic commands ###
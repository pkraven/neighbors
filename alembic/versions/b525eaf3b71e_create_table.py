"""create table

Revision ID: b525eaf3b71e
Revises:
Create Date: 2018-06-24 19:30:05.749338

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2 as ge


# revision identifiers, used by Alembic.
revision = 'b525eaf3b71e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("create extension if not exists postgis;")
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column('coords', ge.Geometry(geometry_type='POINT', srid=4326), nullable=False)
    )


def downgrade():
    op.drop_table('users')
    op.execute("drop extension if exists postgis;")

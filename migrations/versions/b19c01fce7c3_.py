"""empty message

Revision ID: b19c01fce7c3
Revises: 8e77bab60804
Create Date: 2020-07-16 19:48:04.271787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b19c01fce7c3'
down_revision = '8e77bab60804'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'tests', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tests', type_='unique')
    # ### end Alembic commands ###

"""empty message

Revision ID: 049e8c636657
Revises: 40021e97dddc
Create Date: 2020-06-10 16:28:29.220739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '049e8c636657'
down_revision = '40021e97dddc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Actor', ['name'])
    op.create_unique_constraint(None, 'Movie', ['title'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Movie', type_='unique')
    op.drop_constraint(None, 'Actor', type_='unique')
    # ### end Alembic commands ###

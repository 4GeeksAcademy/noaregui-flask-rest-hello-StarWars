"""empty message

Revision ID: fff24971e7ed
Revises: 953f37ba38a7
Create Date: 2024-05-09 07:18:53.954108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fff24971e7ed'
down_revision = '953f37ba38a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('terrain', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.drop_column('terrain')

    # ### end Alembic commands ###

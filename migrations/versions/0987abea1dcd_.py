"""empty message

Revision ID: 0987abea1dcd
Revises: 998defa93feb
Create Date: 2024-05-09 07:45:42.813167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0987abea1dcd'
down_revision = '998defa93feb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('naves', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('model', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('manufacturer', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('cost_in_credits', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('length', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('crew', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('passengers', sa.Integer(), nullable=True))
        batch_op.drop_column('modelo')
        batch_op.drop_column('carga')
        batch_op.drop_column('clase')
        batch_op.drop_column('nombre')
        batch_op.drop_column('capacidad_tripulacion')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('naves', schema=None) as batch_op:
        batch_op.add_column(sa.Column('capacidad_tripulacion', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('nombre', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('clase', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('carga', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('modelo', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
        batch_op.drop_column('passengers')
        batch_op.drop_column('crew')
        batch_op.drop_column('length')
        batch_op.drop_column('cost_in_credits')
        batch_op.drop_column('manufacturer')
        batch_op.drop_column('model')
        batch_op.drop_column('name')

    # ### end Alembic commands ###

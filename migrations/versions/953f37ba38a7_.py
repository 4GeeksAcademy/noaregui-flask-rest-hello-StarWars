"""empty message

Revision ID: 953f37ba38a7
Revises: ccefecf269ab
Create Date: 2024-05-09 07:15:19.685470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '953f37ba38a7'
down_revision = 'ccefecf269ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('diameter', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('rotation_period', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('population', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('climate', sa.String(length=200), nullable=True))
        batch_op.drop_column('clima')
        batch_op.drop_column('poblacion')
        batch_op.drop_column('diametro')
        batch_op.drop_column('periodo_rotacion')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planetas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('periodo_rotacion', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('diametro', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('poblacion', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('clima', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
        batch_op.drop_column('climate')
        batch_op.drop_column('population')
        batch_op.drop_column('rotation_period')
        batch_op.drop_column('diameter')

    # ### end Alembic commands ###

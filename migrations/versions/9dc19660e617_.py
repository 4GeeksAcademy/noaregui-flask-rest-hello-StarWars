"""empty message

Revision ID: 9dc19660e617
Revises: 6fbdf562246e
Create Date: 2024-05-10 17:22:05.899541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dc19660e617'
down_revision = '6fbdf562246e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_constraint('Users_name_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.create_unique_constraint('Users_name_key', ['name'])

    # ### end Alembic commands ###
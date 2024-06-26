"""Add created_at to Idea

Revision ID: cddc0f73bfee
Revises: f6e5e0be3754
Create Date: 2024-06-08 15:30:04.165379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cddc0f73bfee'
down_revision = 'f6e5e0be3754'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('idea', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('idea', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###

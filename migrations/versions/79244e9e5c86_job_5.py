"""job+5

Revision ID: 79244e9e5c86
Revises: c21e22bb42d8
Create Date: 2022-01-13 14:02:44.242133

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '79244e9e5c86'
down_revision = 'c21e22bb42d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('assign_to_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'job', 'vehicle', ['assign_to_id'], ['id'])
    op.drop_column('job', 'assign_to')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('assign_to', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'job', type_='foreignkey')
    op.drop_column('job', 'assign_to_id')
    # ### end Alembic commands ###

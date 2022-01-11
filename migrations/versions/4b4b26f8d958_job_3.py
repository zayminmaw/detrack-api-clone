"""job+3

Revision ID: 4b4b26f8d958
Revises: dfa01745aa21
Create Date: 2022-01-11 18:02:51.299123

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '4b4b26f8d958'
down_revision = 'dfa01745aa21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    job_status_enum = postgresql.ENUM('in_progress', 'delivered', 'collected', name='job_status_enum')
    job_status_enum.create(op.get_bind())
    op.add_column('job', sa.Column('status', sa.Enum('in_progress', 'delivered', 'collected', name='job_status_enum'), nullable=True))
    op.add_column('job', sa.Column('priority', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'priority')
    op.drop_column('job', 'status')
    # ### end Alembic commands ###

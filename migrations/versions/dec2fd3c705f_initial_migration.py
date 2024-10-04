"""Initial migration

Revision ID: dec2fd3c705f
Revises: 
Create Date: 2024-10-02 19:54:23.213467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dec2fd3c705f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('designation', sa.String(length=100), nullable=False),
    sa.Column('department', sa.String(length=100), nullable=False),
    sa.Column('date_of_joining', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attendance')
    op.drop_table('employee')
    # ### end Alembic commands ###

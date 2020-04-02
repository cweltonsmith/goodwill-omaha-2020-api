"""Build out rest of the tables

Revision ID: a3f949600f5a
Revises: 09a0cdcdf25a
Create Date: 2020-04-02 15:18:46.945106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3f949600f5a'
down_revision = '09a0cdcdf25a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item_type',
    sa.Column('item_type_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('item_type', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('item_type_id')
    )
    op.create_table('store',
    sa.Column('store_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('store_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('store_id')
    )
    op.create_table('unit_type',
    sa.Column('unit_type_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('unit_type', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('unit_type_id')
    )
    op.create_table('transaction',
    sa.Column('transaction_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('loyalty_id', sa.Integer(), nullable=True),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('tax_year', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['loyalty_id'], ['customer.loyalty_id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['store.store_id'], ),
    sa.PrimaryKeyConstraint('transaction_id')
    )
    op.create_table('transaction_line',
    sa.Column('transaction_line_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('item_type_id', sa.Integer(), nullable=True),
    sa.Column('unit_type_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_type_id'], ['item_type.item_type_id'], ),
    sa.ForeignKeyConstraint(['transaction_id'], ['transaction.transaction_id'], ),
    sa.ForeignKeyConstraint(['unit_type_id'], ['unit_type.unit_type_id'], ),
    sa.PrimaryKeyConstraint('transaction_line_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction_line')
    op.drop_table('transaction')
    op.drop_table('unit_type')
    op.drop_table('store')
    op.drop_table('item_type')
    # ### end Alembic commands ###

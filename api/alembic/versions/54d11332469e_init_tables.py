"""init tables

Revision ID: 54d11332469e
Revises: 
Create Date: 2022-09-01 10:58:11.081077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54d11332469e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meme',
    sa.Column('meme_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=1024), nullable=True),
    sa.Column('link', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('meme_id')
    )
    op.create_table('tag',
    sa.Column('tag_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tag_name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('tag_id')
    )
    op.create_table('tag_meme_association',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('meme_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['meme_id'], ['meme.meme_id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.tag_id'], ),
    sa.PrimaryKeyConstraint('tag_id', 'meme_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag_meme_association')
    op.drop_table('tag')
    op.drop_table('meme')
    # ### end Alembic commands ###

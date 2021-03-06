"""empty message

Revision ID: 221a649b10de
Revises: f7e59be9486d
Create Date: 2020-10-31 03:52:05.545924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '221a649b10de'
down_revision = 'f7e59be9486d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('post_title', sa.String(length=200), nullable=True),
    sa.Column('post_subtitle', sa.String(length=300), nullable=True),
    sa.Column('post_content', sa.Text(), nullable=True),
    sa.Column('post_date', sa.DateTime(), nullable=True),
    sa.Column('post_was_edited', sa.Boolean(), nullable=True),
    sa.Column('post_archived', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('about', sa.String(length=200), nullable=True),
    sa.Column('subtitle', sa.String(length=40), nullable=True),
    sa.Column('website', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('post')
    # ### end Alembic commands ###

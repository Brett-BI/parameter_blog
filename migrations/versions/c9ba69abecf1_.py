"""empty message

Revision ID: c9ba69abecf1
Revises: 6f9c8cf70358
Create Date: 2020-11-03 20:29:18.920964

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = 'c9ba69abecf1'
down_revision = '6f9c8cf70358'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ARTICLE',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('AUTHOR', sa.Integer(), nullable=True),
    sa.Column('TITLE', sa.String(length=200), nullable=False),
    sa.Column('SUBTITLE', sa.String(length=300), nullable=True),
    sa.Column('CONTENT_MARKDOWN', sa.Text(), nullable=True),
    sa.Column('CONTENT_HTML', sa.Text(), nullable=True),
    sa.Column('POSTED_DATE', sa.DateTime(), nullable=False),
    sa.Column('EDITED', sa.Boolean(), nullable=False),
    sa.Column('ARCHIVED', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['AUTHOR'], ['user.id'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('post_id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('post_title', sa.VARCHAR(length=200, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('post_subtitle', sa.VARCHAR(length=300, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('post_content', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('post_date', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.Column('post_was_edited', mssql.BIT(), autoincrement=False, nullable=True),
    sa.Column('post_archived', mssql.BIT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('post_id', name='PK__post__3ED7876691F33FCB')
    )
    op.drop_table('ARTICLE')
    # ### end Alembic commands ###

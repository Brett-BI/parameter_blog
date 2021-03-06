"""empty message

Revision ID: 8a59829c27ae
Revises: c9ba69abecf1
Create Date: 2020-11-11 18:19:49.738670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a59829c27ae'
down_revision = 'c9ba69abecf1'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('FK__ARTICLE__AUTHOR__2A4B4B5E', 'ARTICLE', type_='foreignkey')
    op.drop_table('user')
    
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('USER',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('NAME', sa.String(length=150), nullable=True),
    sa.Column('EMAIL', sa.String(length=120), nullable=False),
    sa.Column('PASSWORD', sa.String(length=200), nullable=False),
    sa.Column('ABOUT', sa.String(length=100), nullable=True),
    sa.Column('PERSONAL_WEBSITE', sa.String(length=200), nullable=True),
    sa.Column('CREATED', sa.DateTime(), nullable=True),
    sa.Column('CLOSED', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    
    op.create_foreign_key(None, 'ARTICLE', 'USER', ['AUTHOR'], ['ID'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ARTICLE', type_='foreignkey')
    op.create_foreign_key('FK__ARTICLE__AUTHOR__2A4B4B5E', 'ARTICLE', 'user', ['AUTHOR'], ['id'])
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('first_name', sa.VARCHAR(length=150, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=150, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=200, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('about', sa.VARCHAR(length=200, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('subtitle', sa.VARCHAR(length=40, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('website', sa.VARCHAR(length=200, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('created', sa.DATETIME(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK__user__3213E83F95812287')
    )
    op.drop_table('USER')
    # ### end Alembic commands ###

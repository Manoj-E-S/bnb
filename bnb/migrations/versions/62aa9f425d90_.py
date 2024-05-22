"""empty message

Revision ID: 62aa9f425d90
Revises: a425f4bd2dc2
Create Date: 2024-05-22 13:21:53.585801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62aa9f425d90'
down_revision = 'a425f4bd2dc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_messages')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_messages',
    sa.Column('uId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('mId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['mId'], ['messages.mId'], name='user_messages_mId_fkey'),
    sa.ForeignKeyConstraint(['uId'], ['users.uId'], name='user_messages_uId_fkey'),
    sa.PrimaryKeyConstraint('uId', 'mId', name='user_messages_pkey')
    )
    # ### end Alembic commands ###
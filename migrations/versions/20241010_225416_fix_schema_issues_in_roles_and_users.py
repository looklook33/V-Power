"""Fix schema issues in roles and users

Revision ID: 0b4c115420db
Revises: 
Create Date: 2024-10-10 22:54:16.015594

"""
from alembic import op
import sqlalchemy as sa


import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = '0b4c115420db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('equipment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('describe', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('galleries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('describe', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('isMember', sa.Boolean(), nullable=True),
    sa.Column('isTrainer', sa.Boolean(), nullable=True),
    sa.Column('isManager', sa.Boolean(), nullable=True),
    sa.Column('describe', sa.String(length=255), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('describe', sa.String(length=255), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('startTime', sa.Time(), nullable=False),
    sa.Column('endTime', sa.Time(), nullable=False),
    sa.Column('create_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedule_users',
    sa.Column('schedule_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['schedule_id'], ['schedules.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('schedule_id', 'user_id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule_users')
    op.drop_table('schedules')
    op.drop_table('roles')
    op.drop_table('galleries')
    op.drop_table('equipment')
    op.drop_table('users')
    # ### end Alembic commands ###

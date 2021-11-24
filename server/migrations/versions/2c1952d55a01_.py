"""empty message

Revision ID: 2c1952d55a01
Revises: 
Create Date: 2021-11-24 13:39:51.926740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c1952d55a01'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('category_l', sa.String(length=32), nullable=True),
    sa.Column('category_m', sa.String(length=32), nullable=True),
    sa.Column('category_s', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('nickname', sa.String(length=128), nullable=True),
    sa.Column('img', sa.String(length=1024), nullable=True),
    sa.Column('intro', sa.Text(), nullable=True),
    sa.Column('exp', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('img', sa.String(length=1024), nullable=True),
    sa.Column('views', sa.Integer(), nullable=False),
    sa.Column('like', sa.Integer(), nullable=False),
    sa.Column('servings', sa.String(length=32), nullable=False),
    sa.Column('difficulty', sa.String(length=32), nullable=False),
    sa.Column('cooking_time', sa.String(length=32), nullable=False),
    sa.Column('food_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['food_id'], ['food.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post', sa.String(length=128), nullable=False),
    sa.Column('img', sa.String(length=1024), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_ingredent',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('amount', sa.String(length=64), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_like',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_process',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('recipe', sa.Text(), nullable=False),
    sa.Column('step', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=1024), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_process')
    op.drop_table('recipe_like')
    op.drop_table('recipe_ingredent')
    op.drop_table('post')
    op.drop_table('recipe')
    op.drop_table('user')
    op.drop_table('food')
    # ### end Alembic commands ###

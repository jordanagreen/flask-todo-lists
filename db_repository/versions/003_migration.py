from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
todo_list = Table('todo_list', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=100)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

todo_list = Table('todo_list', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=100)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['todo_list'].columns['name'].drop()
    post_meta.tables['todo_list'].columns['title'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['todo_list'].columns['name'].create()
    post_meta.tables['todo_list'].columns['title'].drop()

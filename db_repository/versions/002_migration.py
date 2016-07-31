from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
list_item = Table('list_item', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime),
    Column('text', String(length=150)),
    Column('list_id', Integer),
)

todo_list = Table('todo_list', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=100)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['list_item'].create()
    post_meta.tables['todo_list'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['list_item'].drop()
    post_meta.tables['todo_list'].drop()

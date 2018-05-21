# -*- coding: utf-8 -*-

from sqlite_alchemy import Alchemy, Table, Column, MetaData
from exceptions import *

base = Alchemy('my_data_base.db')
conn = base.create_conn()
metadata = MetaData()

user = Table('user', metadata,
             Column('id', 'INTEGER', primary_key=True),
             Column('username', 'TEXT', 'NOT NULL')
             )

posts = Table('posts', metadata,
              Column('id', 'KEY', primary_key=True),
              Column('text', 'TEXT', 'NOT NULL')
              )

# try:
#     # user.create()
#     posts.create()
#     user.select('id', 'username')
# except SqliteAlchemyError as err:
#     print(err)

try:
    # metadata.create_all(conn)
    user.insert(conn, {'username': 'Smith', 'id': '2'})
    # user.drop(conn)
    # posts.drop(conn)
except SqliteAlchemyError as err:
    print(err)

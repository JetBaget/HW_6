from another_way.sqlite_orm import Base
import sqlite3


class User(Base):
    __tablename__ = 'posts'

    id = ('int', 'required')
    username = ('char(256)', 'not_required')


conn = sqlite3.connect('my_data_base.db')
# User(id=1, username='doe', connection=conn).select_all()
# User(id=1, username='doe', connection=conn).create_table()
User(connection=conn).drop()

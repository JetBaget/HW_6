# -*- coding: utf-8 -*-

import sqlite3
from exceptions import *


class Alchemy:
    def __init__(self, db_name=None):
        self.db_name = db_name
        self.conn = None

    def create_conn(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
        except sqlite3.Error as err:
            raise CreateConnError(err)
        return self.conn


class Table:
    def __init__(self, table_name, metadata, *args):
        self.name = table_name
        metadata._tables[table_name] = args

    def send_query(self, conn, q):
        try:
            conn.execute(q)
        except sqlite3.OperationalError as err:
            raise SqliteAlchemyError(err)

    def select(self, conn, *args):
        q = 'SELECT {} FROM {};'.format(', '.join(args), self.name)
        print(q)
        self.send_query(conn, q)

    def insert(self, conn, data):
        vals = ['\'{}\''.format(v) for v in data.values()]
        q = 'INSERT INTO {} ({}) VALUES ({});'.format(self.name,
                                                          ', '.join(data.keys()),
                                                          ', '.join(vals))
        print(q)
        self.send_query(conn, q)
        conn.commit()

    def drop(self, conn):
        q = 'DROP TABLE {};'.format(self.name)
        print(q)
        self.send_query(conn, q)
        conn.commit()


class Column:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.primary = kwargs.get('primary_key')

    def __str__(self):
        col_text = ' '.join(self.args)
        if self.primary:
            ' '.join([col_text, 'PRIMARY KEY'])
        return col_text


class MetaData:
    def __init__(self):
        self._tables = dict()

    def create_all(self, conn):
        try:
            for t_name in self._tables:
                columns = [str(col) for col in self._tables[t_name]]
                q = 'CREATE TABLE {} ({});'.format(t_name, ', '.join(columns))
                print(q)
                conn.execute(q)
                conn.commit()
            self._tables = dict()
        except sqlite3.OperationalError as err:
            raise SqliteAlchemyError(err)

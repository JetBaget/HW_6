# -*- coding: utf-8 -*-


class SqliteAlchemyError(Exception):
    def __init__(self, message=None):
        self.message = 'Ошибка SqliteAlchemy. {}'.format(message)

    def __str__(self):
        return self.message


class CreateConnError(SqliteAlchemyError):
    def __init__(self, message=None):
        self.message = 'Ошибка подключения к БД. {}'.format(message)

    def __str__(self):
        return self.message

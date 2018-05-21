# -*- coding: utf-8 -*-


class Base:
    def __init__(self):
        pass

    def select_all(self):
        field_names = [k for k in self.__class__.__dict__.keys() if not k.startswith('__')]
        print('SELECT %s FROM %s;' % (', '.join(field_names), self.__class__.__tablename__))

    def create_table(self):
        name = self.__class__.__tablename__
        field_names = [k for k in self.__class__.__dict__.keys() if not k.startswith('__')]

        q = 'CREATE TABLE {} ({})'.format(name, )
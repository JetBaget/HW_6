# -*- coding: utf-8 -*-


class Base:
    def __init__(self, **kwargs):
        self.conn = kwargs.get('connection')
        self.name = self.__class__.__tablename__

    def select_all(self):
        field_names = [k for k in self.__class__.__dict__.keys() if not k.startswith('__')]
        print('SELECT %s FROM %s;' % (', '.join(field_names), self.__class__.__tablename__))

    def create_table(self):
        fields = [k for k in self.__class__.__dict__.items() if not k[0].startswith('__')]
        parsed_fields = [self._parse_field(f) for f in fields]
        q = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(self.name, ', '.join(parsed_fields))
        self.send_query(q)
        self.conn.commit()

    def send_query(self, q):
        self.conn.execute(q)

    def _parse_field(self, field):
        data_types = {'char': 'TEXT', 'int': 'INTEGER'}
        field_name = field[0]
        field_type = data_types[field[1][0].split('(')[0]].strip(' ')
        result = ' '.join([field_name, field_type])
        if 'required' in field[1]:
            result = ' '.join([result, 'NOT NULL'])
        if 'primary_key' in field[1]:
            result = ' '.join([result, 'PRIMARY KEY'])
        return result

    def drop(self):
        q = 'DROP TABLE IF EXISTS {}'.format(self.name)
        self.send_query(q)

    def insert(self):
        q = 'INSERT INTO {} ({}) VALUES ({})'.format(self.name, )

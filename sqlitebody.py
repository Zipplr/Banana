import sqlite3
from datetime import datetime

class SQLbody():
    
    """
    Module for E-zy SQLite3 data bases manipulating
    version 0.1 from 29.06.16
    functions:
        insert - insert new values in existed data base
        create - create new table
        show - show and return values from data base
        close - close connection with data base
    """
    
    def __init__(self, path):
        self.session_start = datetime.now()
        self.path = path
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        print('Session starts at %s, storage path: %s' % (self.session_start, self.path))

    def insert(self, table, values1, values2):
        const_values =  ''
        new_values = ''
        for i in values1:
            const_values += i + ','
        for j in values2:
            new_values += j + ','
        const_values = const_values[0:-1]
        new_values = new_values[0:-1]
        request = "insert into %s (%s) values (%s)" % (table, const_values, new_values)
        print(request)
        self.cursor.execute(request)
        self.connection.commit()

    def create(self, table, values):
        new_values = ''
        for i in values:
            new_values += i + ','
        new_values = new_values[0:-1]
        request = "create table %s (%s)" % (table, new_values)
        print(request)
        self.cursor.execute(request)
        self.connection.commit()
        
    def show(self, query='select * from root', where=''):
        for i in self.cursor.execute(query + ' ' + where):
            print(i)
        return self.cursor.execute(query + ' ' + where)

    def close(self):
        session_end = datetime.now()
        self.connection.close()
        session_time = str(session_end - self.session_start)
        print('Connection has been closed. Session time: %s' % (session_time))

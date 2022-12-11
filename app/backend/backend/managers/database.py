import sqlite3
from .. import env

class Database():

    class QueryHandler():
        def __init__(self):
            self.queries = []

        def appendQuery(self, query, params=[]):
            self.queries.append((query, params))

    def __init__(self):
        self.db = self._init_db()
        self.curs = self._open_cursor()

    def execute(self, query, params=[]):
        self.curs.execute(query, params)
        return self

    def commit(self):
        self.db.commit()
        self.curs.close()
        self.db.close()

    def fetchone(self):
        result = self.curs.fetchone()
        self.curs.close()
        self.db.close()
        return result

    def fetchall(self):
        result = self.curs.fetchall()
        self.curs.close()
        self.db.close()
        return result

    def _init_db(self):
        return sqlite3.connect(env.DATABASE_NAME)

    def _open_cursor(self):
        return self.db.cursor()

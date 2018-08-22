import sqlite3

class DBStore:
    def __init__(self, dbfile = "mylist.sqlite"):
        self.dbfile = dbfile
        self.conn = sqlite3.connect(dbfile)
        self.c = self.conn.cursor()

    def create_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS items (description text)")
        self.conn.commit()

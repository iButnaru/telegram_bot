import sqlite3

class DBStore:
    def __init__(self, dbfile = "mylist.sqlite"):
        self.dbfile = dbfile
        self.conn = sqlite3.connect(dbfile)
        self.c = self.conn.cursor()

    def create_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS items (description text)")
        self.conn.commit()

    def add_items(self, item):
        args = item
        self.conn.execute("INSERT INTO items (description) VALUES (?)",
        (args,))
        self.conn.commit()

    def delete_items(self, item):
        args = item
        self.conn.execute("DELETE FROM items WHERE description = (?)",
                          (args,))
        self.conn.commit()

    def get_item(self):
        stmt = "SELECT description FROM items"
        return [x[0] for x in self.conn.execute(stmt)]



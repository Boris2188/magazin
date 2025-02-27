from magazin_project.database import get_connect


class DataBaseControl:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = get_connect()
        return self.conn

    def add_product(self, params=None):
        insert_query = ("""INSERT INTO products (tovar, cena, kolicestvo) 
        VALUES (?, ?, ?);""")
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(insert_query, (params))
            con.commit()

    def view_all(self):
        view_query = ("""SELECT * FROM products""")
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(view_query)
            rows = cur.fetchall()
            for row in rows:
                print(row)




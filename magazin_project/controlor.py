from magazin_project.database import get_connect


class DataBaseControl:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = get_connect()
        return self.conn

    def add_product(self, product, price, quantity):
        insert_query = ("""INSERT INTO products (tovar, cena, kolicestvo) 
        VALUES (?, ?, ?);""")
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(insert_query, (product, price, quantity))
            con.commit()




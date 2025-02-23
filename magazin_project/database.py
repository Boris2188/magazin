import sqlite3
from contextlib import contextmanager


with sqlite3.connect("magazin.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS products(
    tovar TEXT,
    cena INTEGER,
    kolicestvo INTEGER
    )""")


@contextmanager
def get_connect():
    conn = sqlite3.connect("magazin.db")
    try:
        yield conn
    finally:
        conn.close()
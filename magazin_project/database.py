import sqlite3
from contextlib import contextmanager

def creat_table():
    with sqlite3.connect("magazin.db") as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS products(
        tovar TEXT,
        cena INTEGER,
        kolicestvo INTEGER
        )""")
        print("Таблица магазин создана")


@contextmanager
def get_connect():
    conn = sqlite3.connect("magazin.db")
    try:
        yield conn
    except Exception as e:
        print(e)
    finally:
        conn.close()



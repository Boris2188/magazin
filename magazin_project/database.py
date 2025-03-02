import sqlite3
from contextlib import contextmanager

def creat_table():
    with sqlite3.connect("magazin.db") as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS products(
        tovar TEXT,
        cena REAL,
        kolicestvo INTEGER
        )""")
        print("Таблица магазин создана")

        cur.execute("""CREATE TABLE IF NOT EXISTS sales_report(
        tovar TEXT,
        kolicestvo_prodaz INTEGER,
        suma_prodaz REAL)
        """)


@contextmanager
def get_connect():
    conn = sqlite3.connect("magazin.db")
    try:
        yield conn
    except Exception as e:
        print(e)
    finally:
        conn.close()



from magazin_project.database import get_connect


class DataBaseControl:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = get_connect()
        return self.conn

    def add_product(self, params=None):
        if not params or len(params) != 3:
            print("Ошибка: Необходимо передать 3 параметра (название, цена, количество).")
            return
        insert_query = """
        INSERT INTO products (tovar, cena, kolicestvo) 
        VALUES (?, ?, ?);
        """
        with self.connect() as con:
            cur = con.cursor()
            try:
                cur.execute(insert_query, tuple(params))
                con.commit()
                print(f"Товар '{params[0]}' успешно добавлен.")
            except sqlite3.Error as e:
                print(f"Ошибка при добавлении товара: {e}")

    def view_all(self):
        view_query = """
        SELECT * FROM products
        """
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(view_query)
            rows = cur.fetchall()
            for row in rows:
                print(row)

    def check_product_quantity(self, params=None ):
        if not params or len(params) < 2:
            print("Ошибка: Недостаточно параметров.")
            return

        query_select ="""
        SELECT tovar, cena, kolicestvo FROM products
        WHERE tovar = ? AND kolicestvo >= ?
        """
        query_update = """
        UPDATE products SET kolicestvo = ? WHERE tovar = ?
        """
        query_insert = """
        INSERT INTO sales_report (tovar,kolicestvo_prodaz,
        suma_prodaz) VALUES (?, ?, ?)
        """
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(query_select, (params[0], params[1]))
            value = cur.fetchone()

            if not value:
                print("Ошибка: Товар не найден или недостаточное количество.")
                return
            tovar, price, available_quantity = value
            requested_quantity = params[1]
            print(f"\nТовар {tovar}, имеет {available_quantity} шт. в наличии!")
            if available_quantity >= requested_quantity:
                new_quantity = available_quantity - requested_quantity
                cur.execute(query_update, (new_quantity, tovar))
                total_cost = price * requested_quantity
                cur.execute(query_insert, (tovar, requested_quantity, total_cost))
                con.commit()
                print(f"Продажа успешно завершена. Общая сумма: {total_cost} руб.")
            else:
                print("Ошибка: Недостаточно товара в наличии.")


    def gene_sales_report(self):

        query_select = """
        SELECT tovar, kolicestvo_prodaz,suma_prodaz
        FROM sales_report"""
        query_select_sum = """
        SELECT SUM(suma_prodaz) FROM sales_report
        """
        with self.connect() as con:
            cur = con.cursor()
            cur.execute(query_select)
            tottal_sales = cur.fetchone()[0]
            cur.execut(query_select_sum)
            sels_list = cur.fetchall()
            return (tottal_sales,sels_list)
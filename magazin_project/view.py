class Output:
    def welcome(self):
        print(f"Добропожаловать в магазин!")

    def show_options(self):
        print(f"\nВыберите действие:\n"
              f"1.Добавление новых товаров в магазин\n"
              f"2.Просмотр списка товаров в магазине:\n"
              f"3.Продажа товаров\n"
              f"4.Генерация отчета о продажах\n"
              f"5.Выход")

    def show_first_option(self):
        while True:
            try:
                product = input("Введите название товара: ").strip()
                if not product:
                    print("Ошибка: Название товара не может быть пустым.")
                    continue

                price = float(input("Введите цену: "))
                if price < 0:
                    print("Ошибка: Цена не может быть отрицательной.")
                    continue

                quantity = int(input("Введите количество: "))
                if quantity < 0:
                    print("Ошибка: Количество не может быть отрицательным.")
                    continue

                return (product, price, quantity)
            except ValueError:
                print("Ошибка: Введены некорректные данные. Пожалуйста, попробуйте снова.")

    def user_action(self) -> int:
        while True:
            try:
                action = int(input("Введите действие: "))
                if action == 5:
                    print("Выход из программы...")
                    return 5
                if 1 <= action <= 4:
                    return action
                else:
                    print("Ошибка: Введите число от 1 до 4.")

            except ValueError:
                print("Ошибка: Введены некорректные данные. Пожалуйста, введите число.")

    def info_select_product(self):
        print("Выберите продукт и укажите количество: ")

    def select_product(self):
        while True:
            try:
                product = input("Введите наименование продукта: ").strip()
                if not product:
                    print("Ошибка: Название товара не может быть пустым.")
                    continue
                quantity = int(input("Введите количество: "))
                if quantity <= 0:
                    print("Ошибка: Количество должно быть положительным числом.")
                    continue

                return (product, quantity)
            except ValueError:
                print("Ошибка: Введены некорректные данные. Пожалуйста, введите число для количества.")

    def view_selse_report(self, params=None):
        if not params or len(params) != 2:
            print("Ошибка: Некорректные данные для отчета.")
            return
        self.tottal_summ = params[0]
        self.list_sale = params[1]
        print("\nОтчот о продажах:")
        print(f"Общая сумма всех продаж: {self.tottal_summ} руб.")
        print('Список проданых товаров:')
        for sale in self.list_sale:
            product , quantity, price = sale
            print(f"Товар: {product}, Количество: {quantity}, Сумма: {price} руб.")

class Output:
    def welcome(self):
        print(f"Добропожаловать в магазин!")

    def show_options(self):
        print(f"\nВыберите действие:\n"
              f"1.Добавление новых товаров в магазин\n"
              f"2.Просмотр списка товаров в магазине:\n"
              f"3.Продажа товаров\n"
              f"4.Генерация отчета о продажах\n")

    def show_first_option(self):
        product = input("Введите название товара: ")
        price = float(input("Ведите цену: "))
        quntity = int(input("Ведите количество:" ))
        a = (product, price, quntity)
        return a


    def user_action(self) -> int:
        action = int(input("Введите действие: "))
        return action
from magazin_project import view
from  magazin_project.database import creat_table
from magazin_project.controlor import DataBaseControl
import time

view = view.Output()
control = DataBaseControl()

def first_action():
    """Добавление товара."""
    product_data = view.show_first_option()
    control.add_product(product_data)


def second_action():
    """Просмотр всех товаров."""
    control.view_all()

def third_action():
    """Продажа товара."""
    product_data = view.info_select_product()
    a = view.select_product()
    control.check_product_quantity(a)

def fourth_action():
    """Генерация отчета о продажах."""
    report_data = control.gene_sales_report()
    view.view_selse_report(report_data)

def start():
    """Основная функция для запуска программы."""
    view.welcome()
    while True:
        view.show_options()
        action = view.user_action()
        if action == 1:
            first_action()
        elif action == 2:
            second_action()
            time.sleep(3)
        elif action == 3:
            third_action()
            time.sleep(2)
        elif action == 4:
            fourth_action()
        elif action == 5:
            print("Выход из программы...")
            break
        else:
            print("Ошибка: Неверный выбор. Пожалуйста, выберите действие от 1 до 5.")


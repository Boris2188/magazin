from magazin_project import view
from  magazin_project.database import creat_table
from magazin_project.controlor import DataBaseControl
import time

view = view.Output()
control = DataBaseControl()
action = None

def first_action():
    a = view.show_first_option()
    control.add_product(a)

def second_action():
    control.view_all()

def start():
    creat_table()
    view.welcome()
    while True:
        view.show_options()
        action = view.user_action()
        if action == 1:
            first_action()
            continue
        elif action == 2:
            second_action()
            time.sleep(3)
            continue





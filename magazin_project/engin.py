from magazin_project import view
from  magazin_project.database import creat_table
from magazin_project.controlor import DataBaseControl

view = view.Output()
control = DataBaseControl()

def start():
    creat_table()
    view.welcome()
    view.sow_options()
    control.add_product('джинсы', 1500, 12)


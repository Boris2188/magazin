from magazin_project.engin import start
from magazin_project.database import creat_table


def main():
    creat_table()
    start()


if __name__ == "__main__":
    main()
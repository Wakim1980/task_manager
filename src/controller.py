import os

from src.menu import Menu


class Controller:
    def __init__(self):
        self._flag = True

    def run(self):
        menu = Menu()
        menu.add_menu_item("добавить задачу", None)
        menu.add_menu_item("изменить задачу", None)
        menu.add_menu_item("удалить задачу", None)
        menu.add_menu_item("показать все не заверешенные задачи", None)
        menu.add_menu_item("показать все задачу важные задачи на дату", None)
        menu.add_menu_item("показать все важные задачи", None)
        menu.add_menu_item("показать детали задачи", None)
        menu.add_menu_item("Поиск задачи по тексту", None)
        menu.add_menu_item("закрыть программу", self._stop)
        while self._flag:
            os.system("cls")
            menu.show()
            menu.get_value_from_input("Выберите пункт меню ")()
            os.system("pause")

    def add_task(self):

        pass

    def update_task(self):
        pass

    def delete_task(self):
        pass

    def show_unfinished_task(self):
        pass

    def show_all_task_by_date(self):
        pass

    def show_priority_tasks(self):
        pass

    def show_task_details(self):
        pass

    def show_tasks_by_text(self):
        pass

    def _stop(self):
        self._flag = False



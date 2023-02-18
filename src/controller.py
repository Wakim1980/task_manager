import os
from datetime import datetime

from src.menu import Menu
from src.taskrepository import TaskRepository
from src.task import Task


class Controller:
    def __init__(self):
        self._flag = True
        self._repository: TaskRepository = TaskRepository()

    def run(self):
        menu = Menu()
        menu.add_menu_item("добавить задачу", self.add_task)
        menu.add_menu_item("изменить задачу", self.update_task)
        menu.add_menu_item("удалить задачу", self.delete_task)
        menu.add_menu_item("показать все не заверешенные задачи", self.show_unfinished_task)
        menu.add_menu_item("показать все важные задачи ", self.show_priority_tasks)
        menu.add_menu_item("показать детали задачи", self.show_task_details)
        menu.add_menu_item("Поиск задачи по тексту", self.show_tasks_by_text)
        menu.add_menu_item("закрыть программу", self._stop)
        while self._flag:
            os.system("cls")
            menu.show()
            menu.get_value_from_input("Выберите пункт меню ")()
            os.system("pause")

    def add_task(self):
        menu = Menu()
        name: str = input("название задачи ")
        menu.add_menu_item("важная задача ", True)
        menu.add_menu_item("не важная задача ", False)
        menu.show()
        priority: bool = menu.get_value_from_input("Выберите пункт меню ")
        description: str = input("описание ")
        execution_date = input("Укажите конечную дату выполнения ").split(".")
        execution_date = datetime(*[int(i) for i in execution_date])
        task = Task(-1, name, priority, description, execution_date)
        task = self._repository.add(task)
        print("Задача добавлена " if task.id >= 0 else "не получилось добавить задачу")

    def update_task(self):
        user_input = int(input("Введите номер задачи "))
        temp: Task = self._repository.find_by_id(user_input)
        menu = Menu()
        menu.add_menu_item("Изменить название ", 1)
        menu.add_menu_item("Изменить важность ", 2)
        menu.add_menu_item("Изменить описание ", 3)
        menu.add_menu_item("Изменить дату выполнения ", 4)
        menu.add_menu_item("Завершить ", 5)
        while True:
            menu.show()
            user_input = menu.get_value_from_input("Выберите пункт меню ")
            if user_input == 5:
                break
            match user_input:
                case 1:
                    temp.name = input("Новое название задачи -> ")
                case 2:
                    temp.priority = True if input("Важная 1 ,Не важная 2 ") == "1" else False
                case 3:
                    temp.description = input("Новое Описание -> ")
                case 4:
                    temp.execution_date = input("Новая дата ").split(".")
                    temp.execution_date = datetime(*[int(i) for i in temp.execution_date])
        print("Задача изменена" if self._repository.update(temp) else "ERROR")

    def delete_task(self):
        user_input = int(input("Введите номер задачи, которую нужно удалить "))
        print("Задача удалена" if self._repository.remove(user_input) else "Не получилось удалить задачу")

    def show_unfinished_task(self):
        temp = self._repository.get_all()
        result: list[Task] = []
        for i in temp:
            if i.task_completed == False:
                result.append(i)
        for i in result:
            print(i)

    def show_all_task_by_date(self, date: datetime):
        temp = self._repository.get_all()
        result: list[Task] = []
        for i in temp:
            if i.execution_date == date:
                result.append(i)
        for i in result:
            print(i)

    def show_priority_tasks(self):
        temp = self._repository.get_all()
        result: list[Task] = []
        for i in temp:
            if i.priority and not i.task_completed:
                result.append(i)
        for i in result:
            print(i)

    def show_task_details(self):
        user_input = int(input("Введите номер задачи "))
        task = self._repository.find_by_id(user_input)
        print(f"{'номер':<20}{task.id}\n{'название':<20}{task.name}\n{'приоритет':<20}{'ВАЖНО' if task.priority ==1 else 'НЕВАЖНО'}\n{'описание задачи':<20}{task.description}\n{'дата выполнения':<20}{task.execution_date}")

    def show_tasks_by_text(self):
        user_text = input("Введите теск по которому нужно начать поиск ")
        result = self._repository.find_by_text(user_text)
        for i in result:
            print(i)

    def _stop(self):
        self._flag = False



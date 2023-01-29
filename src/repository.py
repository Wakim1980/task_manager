import mysql.connector
import re

from src.task import Task
# добавить деструктор


class Repository:
    def __init__(self):
        self._mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="task_manager")
        self._cursor = self._mydb.cursor()

    def __del__(self):
        self._mydb.close()# деструктор -> магический метод, закрывает соеденение в базу данных

    def add(self, task: Task) -> Task:
        task_tuple = (task.name, task.priority, task.description, task.execution_date)
        self._cursor.execute("insert tasks (name,priority,description,execution_date) values(%s,%s,%s,%s)", task_tuple)
        self._mydb.commit()
        task.id = self._cursor.lastrowid
        return task

    def update(self, task: Task)-> bool:
        self._cursor.execute(f"update tasks set name='{task.name}', priority={task.priority}, description='{task.description}', execution_date='{task.execution_date}' where id={task.id}")
        self._mydb.commit()
        return self._cursor.rowcount > 0

    def remove(self, id: int) -> bool:
        self._cursor.execute(f"delete from tasks where id={id}")
        self._mydb.commit()
        return self._cursor.rowcount > 0

    def find(self, param) -> list[Task]:
        return [i for i in self.get_all() if param(i)]

    def find_by_id(self, id: int) -> Task:
        self._cursor.execute(f"select * from tasks where id={id}")
        temp = self._cursor.fetchone()
        return Task(*temp)

    def get_all(self) -> list[Task]:
        self._cursor.execute("select * from tasks")
        temp = self._cursor.fetchall()
        return [Task(*i) for i in temp]

    def find_by_text(self, text: str):
        t = text.split(" ")
        col = ["name", "description"]
        filter = ""
        for j, x in enumerate(col):
            for i, y in enumerate(t):
                filter = filter + f"{x} like '%{y}%' "
                if i < len(t) - 1:
                    filter = filter + "and "
            if j < len(col) - 1:
                filter = filter + ") or ("
        self._cursor.execute(f"select * from tasks where ({filter})")
        result = self._cursor.fetchall()
        return [Task(*i) for i in result]

    def completed_task(self, id: int)-> bool:
        task = self.find_by_id(id)
        self._cursor.execute(f"update task set task_completed = {task.task_completed} where id ={task.id}")








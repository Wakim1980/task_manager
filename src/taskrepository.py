import mysql.connector
import re

from src.repository_base import RepositoryBase
from src.task import Task
# добавить деструктор


class TaskRepository(RepositoryBase):
    def __init__(self):
        super(TaskRepository, self).__init__()
        self._table_name = "tasks"

    def __del__(self):
        super(TaskRepository, self).__del__()

    def add(self, task: Task):
        column: str = "name,priority,description,execution_date"
        task_tuple = (task.name, task.priority, task.description, task.execution_date)
        task.id = super(TaskRepository, self).add(self._table_name, column, task_tuple)
        return task

    def update(self, task: Task) -> bool:
        return super(TaskRepository, self).update(task.id,self._table_name,("name", "priority", "description", "execution_date"),(task.name, task.priority, task.description, task.execution_date))

    def remove(self, id: int) -> bool:
        return super(TaskRepository, self).remove(self._table_name, id)

    def find(self, param) -> list[Task]:
        return [i for i in self.get_all() if param(i)]

    def find_by_id(self, id: int) -> Task:
        result = super(TaskRepository, self).find_by_id(id,self._table_name)
        if result is None:
            return None
        return Task(*result)

    def get_all(self) -> list[Task]:
        result = super(TaskRepository, self).get_all(self._table_name)
        return [Task(*i) for i in result]

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

    def completed_task(self, id: int):
        task = self.find_by_id(id)
        self._cursor.execute(f"update tasks set task_completed = 1 where id ={task.id}")
        self._mydb.commit()







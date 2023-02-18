from dataclasses import dataclass

from src.task import Task
from src.taskrepository import TaskRepository
from src.user import User
from src.user_repository import UserRepository
from src.user_task_repository import UserTaskRepository


@dataclass
class UserTask:
    user_id: int
    task_id: int

    @staticmethod
    def all_user(id_user) -> list[User]:
        user_task_repository = UserTaskRepository()
        users_task = user_task_repository.get_all_task_user(id_user)
        user_repository = UserRepository()
        users_task = [user_repository.find_by_id(i) for i in users_task]
        return users_task

    @staticmethod
    def all_tasks(id_task) -> list[Task]:
        user_task_repository = UserTaskRepository()
        temp = user_task_repository.get_all_user_tasks(id_task)
        task_repository = TaskRepository()
        result = [task_repository.find_by_id(i) for i in temp]
        return result


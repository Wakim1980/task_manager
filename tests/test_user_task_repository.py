import random

from _pytest.fixtures import fixture

from src.taskrepository import TaskRepository
from src.user_repository import UserRepository
from src.user_task import UserTask
from src.user_task_repository import UserTaskRepository


@fixture
def user_task_repository():
    u_t_r = UserTaskRepository()
    return u_t_r


@fixture
def user_repository():
    user_rep = UserRepository()
    return user_rep


@fixture
def task_repository():
    task_rep = TaskRepository()
    return task_rep


def test_add(user_task_repository,user_repository, task_repository):
    users = user_repository.get_all()
    tasks = task_repository.get_all()
    user_tasks = user_task_repository.get_all()
    while True:
        user = users[random.randrange(len(users))]
        task = tasks[random.randrange(len(tasks))]
        user_task = UserTask(user.id,task.id)
        if user_task not in user_tasks:
            break
    user_task_repository.add(user.id,task.id)
    assert user_task in user_task_repository.get_all()


def test_remove(user_task_repository,user_repository, task_repository):
    users = user_repository.get_all()
    tasks = task_repository.get_all()
    user_tasks = user_task_repository.get_all()
    while True:
        user = users[random.randrange(len(users))]
        task = tasks[random.randrange(len(tasks))]
        user_task = UserTask(user.id, task.id)
        if user_task in user_tasks:
            break
    assert user_task_repository.remove(user.id, task.id) is True


def test_change_user(user_task_repository, user_repository):
    temp = user_task_repository.get_all()[0]
    all_user = user_repository.get_all()
    random_user = all_user[random.randint(0, len(all_user))]
    assert user_task_repository.change_user(temp.task_id,random_user.id) is True


def test_get_all_user_tasks(user_task_repository:UserTaskRepository):
    temp = user_task_repository.get_all()
    users_id = temp[0].user_id
    all_task_user = [i.task_id for i in temp if i.user_id == users_id]
    assert all_task_user == user_task_repository.get_all_user_tasks(users_id)


def test_get_all_task_user(user_task_repository:UserTaskRepository):
    temp = user_task_repository.get_all()
    tasks_id = temp[0].user_id
    all_user_task = [i.user_id for i in temp if i.task_id == tasks_id]
    assert all_user_task == user_task_repository.get_all_task_user(tasks_id)

from datetime import datetime

from _pytest.fixtures import fixture

from src.repository import Repository
from src.task import Task


@fixture
def repository():
    repository = Repository()
    return repository


def test_add(repository):
    task = Task(15,"Уборка",True,"Уборка комнаты",datetime(2023,2,15),False)
    task.id = repository.add(task).id
    new_task = repository.find_by_id(task.id)
    assert task == new_task


def test_update(repository):
    task_test = repository.find_by_text("уборка")[0]
    task_test.description = "Уборка на даче"
    repository.update(task_test)
    task_new = repository.find_by_text("Уборка на даче")[0]
    assert task_new == task_test


def test_remove(repository):
    all_task = repository.find_by_text("Уборка комнаты")
    object_id = all_task[1].id
    repository.remove(object_id)
    task = repository.find_by_id(object_id)
    assert task is None


def test_completed_task(repository):
    repository.completed_task(1)
    task = repository.find_by_id(1)
    assert task.task_completed == True


def test_find(repository):
    def find(x:Task):
        return "Заказ".lower() in x.description.lower() or x.task_completed == True
    result = repository.find(find)
    assert len(result) == 3







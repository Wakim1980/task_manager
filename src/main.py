# from src.controller import Controller
# from src.random_user import RandomUser
#
# # controller = Controller()
# # controller.run()
# random_uzer = RandomUser.generate()
# print(random_uzer)
from src.taskrepository import TaskRepository
from src.user_repository import UserRepository
from src.user_task import UserTask

user = UserRepository().find_by_id(174)
print(user)

all_task_user = UserTask.all_tasks(user.id)
if len(all_task_user) > 0:
    for i in all_task_user:
        print(i)
else:
    print("У юзера нет текущих задач")

print("------------------------------------")
task = TaskRepository().find_by_id(112)
print(task)
result = UserTask.all_tasks(task.id)
if len(result) < 1:
    print("За данной задачей нет закреленных пользователей")
for i in result:
    print(i)
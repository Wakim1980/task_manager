from src.repository_base import RepositoryBase
# from src.user_task import UserTask


class UserTaskRepository(RepositoryBase):
    def __init__(self):
        super(UserTaskRepository, self).__init__()
        self._table_name = "user_task"

    def __del__(self):
        super(UserTaskRepository, self).__del__()

    def add(self, user_id: int, tas_id: int):
        return super(UserTaskRepository, self).add(self._table_name, "user_id, task_id",(user_id, tas_id))

    def remove(self,user_id: int, tas_id: int):
        self._cursor.execute(f"delete from {self._table_name} where user_id = {user_id} and task_id ={tas_id}")
        self._mydb.commit()
        return self._cursor.rowcount > 0

    def change_user(self,id_task:int, id_user: int):
        self._cursor.execute(f"update {self._table_name} set user_id = {id_user} where task_id = {id_task}")
        self._mydb.commit()
        return self._cursor.rowcount > 0

    # def get_all(self):
    #     result = super(UserTaskRepository, self).get_all(self._table_name)
    #     return [UserTask(*i) for i in result]

    def get_all_user_tasks(self, idUser: int)-> list[int]:
        self._cursor.execute(f"select task_id from {self._table_name} where user_id = {idUser}")
        return list(*self._cursor.fetchall())

    def get_all_task_user(self,id_task:int)-> list[int]:
        self._cursor.execute(f"select user_id from {self._table_name} where task_id = {id_task}")
        return list(*self._cursor.fetchall())

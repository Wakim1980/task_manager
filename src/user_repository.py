import mysql.connector

from src.repository_base import RepositoryBase
from src.user import User


class UserRepository(RepositoryBase):
    def __init__(self):
        super(UserRepository, self).__init__()
        self._table_name = "user"

    def __del__(self):
        super(UserRepository, self).__del__()

    def add(self, user: User) -> User:
        user_tuple = (user.login, user.pass_hash,user.last_name,user.first_name, user.email)
        colum = "login,pass_hash,last_name,first_name,email"
        user.id = super(UserRepository, self).add(self._table_name,colum,user_tuple)
        return user

    def remove(self, id: int) -> bool:
        return super(UserRepository, self).remove(self._table_name,id)

    def update(self, user: User) -> bool:
        colum =("last_name", "first_name", "email")
        user_tuple = (user.last_name,user.first_name,user.email)
        return super(UserRepository, self).update(user.id,self._table_name,colum,user_tuple)

    def find_by_id(self, id: int) -> User:
        result = super(UserRepository, self).find_by_id(id,self._table_name)
        if result is None:
            return None
        return User(*result)

    def fin_by_login(self, log: str) -> User:
        self._cursor.execute(f"select * from user where login = '{log}'")
        result = self._cursor.fetchone()
        if result is None:
            return None
        return User(*result)

    def find_by_email(self, email: str) -> User:
        self._cursor.execute(f"select * from user where email = '{email}'")
        result = self._cursor.fetchone()
        if result is None:
            return None
        return User(*result)

    def get_all(self) -> list[User]:
        result = super(UserRepository, self).get_all(self._table_name)
        return [User(*i) for i in result]



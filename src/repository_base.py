from datetime import datetime

import mysql.connector
import sys

from src.task import Task


class RepositoryBase:
    def __init__(self):
        self._mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="task_manager")
        self._cursor = self._mydb.cursor()

    def __del__(self):
        self._mydb.close()

    def add(self, tab_name: str, columns: str, tapl: tuple) -> int:
        values = ",".join(["%s" for i in range(len(tapl))])
        self._cursor.execute(f"insert {tab_name} ({columns}) values({values})", tapl)
        self._mydb.commit()
        return self._cursor.lastrowid

    def remove(self, name_table: str, id: int):
        self._cursor.execute(f"delete from {name_table} where id ={id}")
        self._mydb.commit()
        return self._cursor.rowcount > 0

    def update(self,id: int, name_table: str,columns :tuple, tapl: tuple):
        values = ",".join([f"{c} = '{t}'" if isinstance(t,(str,datetime)) else f"{c} = {t}" for c, t in zip(columns,tapl)])
        self._cursor.execute(f"update {name_table} set {values} where id = {id}")
        self._mydb.commit()
        return self._cursor.rowcount > 0

    def find_by_id(self, id:int, name_table: str):
        self._cursor.execute(f"select * from {name_table} where id ={id}")
        return self._cursor.fetchone()

    def get_all(self,name_table: str):
        self._cursor.execute(f"select * from {name_table}")
        return self._cursor.fetchall()

from .mysql import Mysql
from typing import Dict, List, Any, Tuple


class Crud:
    def __init__(self,
                 db: Mysql,
                 table: str,
                 columns: List[Any]) -> None:
        self.db = db
        self.table = table
        self.columns = columns

    def _get_columns_str(self):
        """
        根据列名自动生成names和values，用于动态拼接SQL语句
        """
        names = ", ".join(self.columns)
        values_ = ["%s" for i in range(len(self.columns))]
        values = ", ".join(values_)
        return names, values

    def _get_insert_sql(self):
        """
        获取新增数据的SQL
        """
        names, values = self._get_columns_str()
        sql = f"INSERT INTO {self.table} ({names}) VALUES ({values})"
        return sql

    async def add(self, *args):
        """
        添加单条数据
        """
        sql = self._get_insert_sql()
        await self.db.execute(sql, values=args)

    async def add_many(self, data: List[Tuple]):
        """
        添加多条数据
        """
        sql = self._get_insert_sql()
        await self.db.execute(sql, data=data)

    async def delete(self, id:int):
        """
        删除单条数据
        """
        sql = f"DELETE FROM {self.table} WHERE id = %s;"
        await self.db.execute(sql, values=[id])


    async def delete_ids(self, ids:Tuple[int]):
        """
        根据ID列表删除多条数据
        """
        ids_=["%s" for _ in range(len(ids))]
        ids_str=", ".join(ids_)
        sql = f"DELETE FROM {self.table} WHERE id IN({ids_str});"
        await self.db.execute(sql, values=ids)

    async def update(self):
        """
        更新单条数据
        """
        pass

    async def update_many(self):
        """
        更新多条数据
        """
        pass

    async def update_ids(self):
        """
        根据ID列表更新多条数据
        """
        pass

    async def find(self):
        """
        查找单条数据
        """
        pass

    async def find_many(self):
        """
        查找多条数据
        """
        pass

    async def find_ids(self):
        """
        根据ID列表查找多条数据
        """
        pass

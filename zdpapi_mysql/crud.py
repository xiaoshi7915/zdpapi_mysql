from .mysql import Mysql
from typing import List, Any

class Crud:
    def __init__(self,
                 db:Mysql,
                 table:str,
                 columns:List[Any]) -> None:
        self.db =db
        self.table = table
        self.columns = columns
    
    def get_columns_str(self):
        """
        根据列名自动生成names和values，用于动态拼接SQL语句
        """
        names = ", ".join(self.columns)
        values_ = ["%s" for i in range(len(self.columns))]
        values = ", ".join(values_)
        return names, values
    
    async def add(self, *args):
        """
        添加单条数据
        """
        names, values = self.get_columns_str()
        sql = f"INSERT INTO {self.table} ({names}) VALUES ({values})"
        await self.db.execute(sql, values=args)
    
    async def add_many(self):
        """
        添加多条数据
        """
        pass
    
    async def delete(self):
        """
        删除单条数据
        """
        pass
    
    async def delete_many(self):
        """
        删除多条数据
        """
        pass
    
    async def delete_ids(self):
        """
        根据ID列表删除多条数据
        """
        pass
    
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
    
    
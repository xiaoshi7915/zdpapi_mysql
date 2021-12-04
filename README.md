# zapi_mysql
基于异步的快速操作MySQL的组件

使用pip安装
```shell
pip install zapi_mysql
```

## 一、增删改数据

### 1.1 创建表
```python
import asyncio
from zapi_mysql import Mysql
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')


async def test_example_execute(loop):
    # 删除表
    await db.connect()
    sql = "DROP TABLE IF EXISTS user;"
    
    # 创建表
    await db.execute(sql)
    sql = """CREATE TABLE user
                                  (id INT,
                                  name VARCHAR(255),
                                  PRIMARY KEY (id));"""
    await db.execute(sql)
    
    # 插入SQL语句
    sql = "INSERT INTO user VALUES(1,'张三')"
    await db.execute(sql)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_execute(loop))
```

### 1.2 插入数据
```python
import asyncio
from zapi_mysql import Mysql
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')


async def test_example_execute(loop):
    # 插入SQL语句
    sql = "INSERT INTO user VALUES(2,'李四')"
    await db.execute(sql)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_execute(loop))
```

### 1.3 批量插入数据
```python
import asyncio
from zapi_mysql import Mysql
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')


async def test_example_execute(loop):
    # 插入SQL语句
    data = [(4, 'gothic metal'), (5, 'doom metal'), (6, 'post metal')]
    sql = "INSERT INTO user VALUES(%s,%s)"
    await db.execute(sql, data=data)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_execute(loop))
```

## 二、查询数据

### 2.1 查询所有数据
```python
import asyncio
from zapi_mysql import Mysql
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')


async def test_example_execute(loop):
    # 插入SQL语句
    sql = "SELECT id, name FROM user ORDER BY id"
    result = await db.execute(sql)
    print("查询结果：\n", result)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_execute(loop))
```

### 2.2 查询单条数据
```python
import asyncio
from zapi_mysql import Mysql
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')


async def test_example_execute(loop):
    # 查询单条数据
    sql = "SELECT id, name FROM user ORDER BY id"
    result = await db.execute(sql, return_all=False)
    print("查询结果：\n", result)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_execute(loop))
```

## 三、CRUD快捷工具

### 3.1 新增用户
```python
import asyncio
from zdpapi_mysql import Mysql, Crud
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')

crud = Crud(db, "user", ["name"])

async def test_create_table(loop):
    # 删除表
    await db.connect()
    sql = "DROP TABLE IF EXISTS user;"

    # 创建表
    await db.execute(sql)
    sql = """CREATE TABLE user(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255));"""
    await db.execute(sql)

    # 插入SQL语句
    sql = "INSERT INTO user VALUES(1,'张三')"
    await db.execute(sql)


async def test_insert(loop):
    # 插入SQL语句
    await crud.add("李四")
    await crud.add("王五")
    await crud.add("赵六")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_create_table(loop))
    loop.run_until_complete(test_insert(loop))

```

### 3.2 添加多条数据
```python
import asyncio
from zdpapi_mysql import Mysql, Crud
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')

crud = Crud(db, "user", ["name"])

async def test_create_table(loop):
    # 删除表
    await db.connect()
    sql = "DROP TABLE IF EXISTS user;"

    # 创建表
    await db.execute(sql)
    sql = """CREATE TABLE user(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255));"""
    await db.execute(sql)

    # 插入SQL语句
    sql = "INSERT INTO user VALUES(1,'张三')"
    await db.execute(sql)


async def test_insert(loop):
    # 插入SQL语句
    await crud.add("李四")
    await crud.add("王五")
    await crud.add("赵六")


async def test_insert_many(loop):
    # 插入SQL语句
    data = [("孙悟空",), ("猪八戒",), ("沙僧",), ]
    await crud.add_many(data)
    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_create_table(loop))
    loop.run_until_complete(test_insert(loop))
    loop.run_until_complete(test_insert_many(loop))

```

### 3.3 根据ID删除数据
```python
import asyncio
from zdpapi_mysql import Mysql, Crud
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')

crud = Crud(db, "user", ["name"])

async def test_create_table(loop):
    # 删除表
    await db.connect()
    sql = "DROP TABLE IF EXISTS user;"

    # 创建表
    await db.execute(sql)
    sql = """CREATE TABLE user(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255));"""
    await db.execute(sql)

    # 插入SQL语句
    sql = "INSERT INTO user VALUES(1,'张三')"
    await db.execute(sql)


async def test_insert(loop):
    # 插入SQL语句
    await crud.add("李四")
    await crud.add("王五")
    await crud.add("赵六")


async def test_insert_many(loop):
    # 插入SQL语句
    data = [("孙悟空",), ("猪八戒",), ("沙僧",), ]
    await crud.add_many(data)
    
async def test_delete(loop):
    # 根据ID删除数据
    await crud.delete(1)
    await crud.delete(2)
    await crud.delete(3)
    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_create_table(loop))
    loop.run_until_complete(test_insert(loop))
    loop.run_until_complete(test_insert_many(loop))
    loop.run_until_complete(test_delete(loop))

```

### 3.4 根据ID列表删除
```python
import asyncio
from zdpapi_mysql import Mysql, Crud
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')

crud = Crud(db, "user", ["name"])

async def test_create_table(loop):
    # 删除表
    await db.connect()
    sql = "DROP TABLE IF EXISTS user;"

    # 创建表
    await db.execute(sql)
    sql = """CREATE TABLE user(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255));"""
    await db.execute(sql)

    # 插入SQL语句
    sql = "INSERT INTO user VALUES(1,'张三')"
    await db.execute(sql)


async def test_insert(loop):
    # 插入SQL语句
    await crud.add("李四")
    await crud.add("王五")
    await crud.add("赵六")


async def test_insert_many(loop):
    # 插入SQL语句
    data = [("孙悟空",), ("猪八戒",), ("沙僧",), ]
    await crud.add_many(data)
    
async def test_delete(loop):
    # 根据ID删除数据
    await crud.delete(1)
    await crud.delete(2)
    await crud.delete(3)
    
async def test_delete_ids(loop):
    # 根据ID列表删除数据
    await crud.delete_ids((3,4,5))
    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_create_table(loop))
    loop.run_until_complete(test_insert(loop))
    loop.run_until_complete(test_insert_many(loop))
    loop.run_until_complete(test_delete(loop))
    loop.run_until_complete(test_delete_ids(loop))
```

### 3.5 更新多条数据
```python
import asyncio
from zdpapi_mysql import Mysql, Crud
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')

crud = Crud(db, "user", ["name"])

async def test_create_table(loop):
    # 删除表
    await db.connect()
    sql = "DROP TABLE IF EXISTS user;"

    # 创建表
    await db.execute(sql)
    sql = """CREATE TABLE user(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255));"""
    await db.execute(sql)

    # 插入SQL语句
    sql = "INSERT INTO user VALUES(1,'张三')"
    await db.execute(sql)


async def test_insert(loop):
    # 插入SQL语句
    await crud.add("李四")
    await crud.add("王五")
    await crud.add("赵六")


async def test_insert_many(loop):
    # 插入SQL语句
    data = [("孙悟空",), ("猪八戒",), ("沙僧",), ]
    await crud.add_many(data)
    
async def test_delete(loop):
    # 根据ID删除数据
    await crud.delete(1)
    await crud.delete(2)
    await crud.delete(3)
    
async def test_delete_ids(loop):
    # 根据ID列表删除数据
    await crud.delete_ids((3,4,5))
    
async def test_update(loop):
    # 根据ID更新数据
    await crud.update(6, {"name":"二郎神111"})
    
async def test_update_many(loop):
    # 更新多条数据
    data=[
        {"id":6, "name":"猪八戒"},
        {"id":7, "name":"嫦娥"},
    ]
    await crud.update_many(data)
   

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_create_table(loop))
    loop.run_until_complete(test_insert(loop))
    loop.run_until_complete(test_insert_many(loop))
    loop.run_until_complete(test_delete(loop))
    loop.run_until_complete(test_delete_ids(loop))
    loop.run_until_complete(test_update(loop))
    loop.run_until_complete(test_update_many(loop))
```

### 3.6 查询单条数据
```python
import asyncio
from zdpapi_mysql import Mysql, Crud
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')

crud = Crud(db, "user", ["name"])

async def test_create_table(loop):
    # 删除表
    await db.connect()
    sql = "DROP TABLE IF EXISTS user;"

    # 创建表
    await db.execute(sql)
    sql = """CREATE TABLE user(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255));"""
    await db.execute(sql)

    # 插入SQL语句
    sql = "INSERT INTO user VALUES(1,'张三')"
    await db.execute(sql)


async def test_insert(loop):
    # 插入SQL语句
    await crud.add("李四")
    await crud.add("王五")
    await crud.add("赵六")


async def test_insert_many(loop):
    # 插入SQL语句
    data = [("孙悟空",), ("猪八戒",), ("沙僧",), ]
    await crud.add_many(data)
    
async def test_delete(loop):
    # 根据ID删除数据
    await crud.delete(1)
    await crud.delete(2)
    await crud.delete(3)
    
async def test_delete_ids(loop):
    # 根据ID列表删除数据
    await crud.delete_ids((3,4,5))
    
async def test_update(loop):
    # 根据ID更新数据
    await crud.update(6, {"name":"二郎神111"})
    
async def test_update_many(loop):
    # 更新多条数据
    data=[
        {"id":6, "name":"猪八戒"},
        {"id":7, "name":"嫦娥"},
    ]
    await crud.update_many(data)

async def test_find_one(loop):
    # 查询单条数据
    result = await crud.find(6)
    print("查询结果：\n", result)
   

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_create_table(loop))
    loop.run_until_complete(test_insert(loop))
    loop.run_until_complete(test_insert_many(loop))
    loop.run_until_complete(test_delete(loop))
    loop.run_until_complete(test_delete_ids(loop))
    loop.run_until_complete(test_update(loop))
    loop.run_until_complete(test_update_many(loop))
    loop.run_until_complete(test_find_one(loop))
```

### 3.8 根据ID列表查询
```python
import asyncio
from zdpapi_mysql import Mysql, Crud
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')

crud = Crud(db, "user", ["name"])


async def test_create_table(loop):
    # 删除表
    await db.connect()
    sql = "DROP TABLE IF EXISTS user;"

    # 创建表
    await db.execute(sql)
    sql = """CREATE TABLE user(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255));"""
    await db.execute(sql)

    # 插入SQL语句
    sql = "INSERT INTO user VALUES(1,'张三')"
    await db.execute(sql)


async def test_insert(loop):
    # 插入SQL语句
    await crud.add("李四")
    await crud.add("王五")
    await crud.add("赵六")


async def test_insert_many(loop):
    # 插入SQL语句
    data = [("孙悟空",), ("猪八戒",), ("沙僧",), ]
    await crud.add_many(data)


async def test_delete(loop):
    # 根据ID删除数据
    await crud.delete(1)
    await crud.delete(2)
    await crud.delete(3)


async def test_delete_ids(loop):
    # 根据ID列表删除数据
    await crud.delete_ids((3, 4, 5))


async def test_update(loop):
    # 根据ID更新数据
    await crud.update(6, {"name": "二郎神111"})


async def test_update_many(loop):
    # 更新多条数据
    data = [
        {"id": 6, "name": "猪八戒"},
        {"id": 7, "name": "嫦娥"},
    ]
    await crud.update_many(data)


async def test_find_one(loop):
    # 查询单条数据
    result = await crud.find(6)
    print("查询结果：\n", result)


async def test_find_ids(loop):
    # 根据ID列表查询
    result = await crud.find_ids([6, 7, 8])
    print("查询结果：\n", result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_create_table(loop))
    loop.run_until_complete(test_insert(loop))
    loop.run_until_complete(test_insert_many(loop))
    loop.run_until_complete(test_delete(loop))
    loop.run_until_complete(test_delete_ids(loop))
    loop.run_until_complete(test_update(loop))
    loop.run_until_complete(test_update_many(loop))
    loop.run_until_complete(test_find_one(loop))
    loop.run_until_complete(test_find_ids(loop))
```

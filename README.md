# zapi_mysql
基于异步的快速操作MySQL的组件

## 一、增删改数据

### 1.1 创建表
```python
import asyncio
from zapi_mysql import Mysql
db = Mysql()


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
db = Mysql()


async def test_example_execute(loop):
    # 插入SQL语句
    sql = "INSERT INTO user VALUES(2,'李四')"
    await db.execute(sql)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_execute(loop))
```


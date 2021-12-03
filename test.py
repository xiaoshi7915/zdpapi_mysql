import asyncio
from zdpapi_mysql import Mysql
db = Mysql(host='127.0.0.1',
           port=3306,
           user='root',
           password='root',
           db='test')


async def test_create_table(loop):
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


async def test_insert(loop):
    # 插入SQL语句
    sql = "INSERT INTO user VALUES(2,'李四')"
    await db.execute(sql)


async def test_insert_many(loop):
    # 插入SQL语句
    data = [(4, 'gothic metal'), (5, 'doom metal'), (6, 'post metal')]
    sql = "INSERT INTO user VALUES(%s,%s)"
    await db.execute(sql, data=data)
    

async def test_find_many(loop):
    # 插入SQL语句
    sql = "SELECT id, name FROM user ORDER BY id"
    result = await db.execute(sql)
    print("查询结果：\n", result)
 
async def test_find_one(loop):
    # 查询单条数据
    sql = "SELECT id, name FROM user ORDER BY id"
    result = await db.execute(sql, return_all=False)
    print("查询结果：\n", result)
   

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_create_table(loop))
    loop.run_until_complete(test_insert(loop))
    loop.run_until_complete(test_insert_many(loop))
    loop.run_until_complete(test_find_many(loop))
    loop.run_until_complete(test_find_one(loop))

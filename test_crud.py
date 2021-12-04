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

async def test_find_page(loop):
    # 分页查询数据
    result = await crud.find_page(1, 20)
    print("查询结果：\n", result)

async def test_find_total(loop):
    # 查询数据总数
    result = await crud.find_total()
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
    loop.run_until_complete(test_find_page(loop))
    loop.run_until_complete(test_find_total(loop))

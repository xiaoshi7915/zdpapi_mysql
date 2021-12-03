import asyncio
import aiomysql


class Mysql:
    def __init__(self,
                 host='127.0.0.1',
                 port=3306,
                 user='root',
                 password='root',
                 db='test') -> None:
        self.loop = asyncio.get_event_loop()
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None

    async def connect(self):
        """
        建立数据库连接
        """
        self.conn = await aiomysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            loop=self.loop)

    async def execute(self, sql: str):
        """
        执行SQL语句
        """
        # 自动建立连接
        if self.conn is None:
            await self.connect()
            
        async with self.conn.cursor() as cur:
            try:
                await cur.execute(sql)
                await self.conn.commit()
            except Exception as e:
                print(e)
                await self.conn.rollback()

    async def create_table(self, sql: str):
        """
        创建数据库表
        """
        await self.execute(sql)

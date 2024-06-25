import  aiosqlite
from database.queries import Queries

class Database:
    def __init__(self, path):
        self.path = path


    async def create_tables(self):
        async with aiosqlite.connect(self.path) as conn:
            async with conn.cursor() as cur:
                # создание всех таблиц
                await cur.execute(Queries.CREATE_REVIEW_TABLE)
                await cur.execute(Queries.DROP_CATEGORIES_TABLE)
                await cur.execute(Queries.DROP_DISHES_TABLE)
                await cur.execute(Queries.CREATE_CATEGORIES_TABLE)
                await cur.execute(Queries.CREATE_DISHES_TABLE)
                await cur.execute(Queries.POPULATE_CATEGORIES_TABLE)
                await cur.execute(Queries.POPULATE_DISHES_TABLE)
                # здесь может быть создание других таблиц
                # которые нам нужны
                await conn.commit()


    async def execute(self, query, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(query, params)
            await conn.commit()


    async def fetch(self, query, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            conn.row_factory = aiosqlite.Row
            data = await conn.execute(query, params)

            result = await data.fetchall()
            return [dict(row) for row in result]


        # connection = sqlite3.connect("db1.sqlite3")
        # cursor = connection.cursor()
        # query = cursor.execute("SELECT * FROM DISHES WHERE category_id = 2")
        # dishes = query.fetchall()


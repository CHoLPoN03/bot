from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from database.database import Database


# подгружаем токен из файла .env
load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
database =Database("db1.sqlite3")

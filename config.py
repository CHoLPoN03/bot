from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv


# подгружаем токен из файла .env
load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    print("Message", message)
    print("User info", message.from_user)

    name = message.from_user.first_name
    await message.answer(f"Привет, {name}")

@dp.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    print("Message", message)
    print("User info", message.from_user)

    user_id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(
        f"Ваш id: {user_id}\n"
        f"Ваше имя: {name}\n"
        f"Ваше имя пользователя: @{username}"
    )

@dp.message(Command("random"))
async def random_pic_handler(message: types.Message):
    file1 = FSInputFile('images/dog.jpg')
    file2 = FSInputFile('images/cat.jpg')
    file3 = FSInputFile('images/horse.jpg')
    await message.answer_photo(file1)
    await message.answer_photo(file2)
    await message.answer_photo(file3)

@dp.message()
async def echo_handler(message: types.Message):
    await message.reply(message.text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
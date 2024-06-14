import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging


from config import dp, bot
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random import random_pic_router
from handlers.echo import echo_router
from handlers.review import review_router
from handlers.menu import menu_category_router

async def main():
    # регистрируем роутеры
    dp.include_router(start_router)
    dp.include_router(random_pic_router)
    dp.include_router(myinfo_router)
    dp.include_router(review_router)
    dp.include_router(menu_category_router)
    dp.include_router(echo_router)
    # запускаем бот
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
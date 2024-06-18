import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging



from config import dp, bot, database
from handlers import (
    start_router,
    echo_router,
    review_router,
    random_pic_router,
    menu_category_router,
    myinfo_router
)


async def on_startup(bot):
    await database.create_tables()

async def main():
    # регистрируем роутеры
    dp.include_router(start_router)
    dp.include_router(random_pic_router)
    dp.include_router(myinfo_router)
    dp.include_router(review_router)
    dp.include_router(menu_category_router)
    dp.include_router(echo_router)
    # запускаем бот
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
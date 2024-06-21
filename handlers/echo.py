from aiogram import Router, types

echo_router = Router()
@echo_router.message()
async def echo_handler(message: types.Message):
    await message.reply("Я Вас не понимаю. Вот команды, которые я понимаю:"
                        "\n/start - начало\n /random - получить картинку\n /myinfo - получить информацию\n"
                        " /review - оставить отзыв\n /menu_category - категории меню"
                        )

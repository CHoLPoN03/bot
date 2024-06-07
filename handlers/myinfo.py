from aiogram import Router, types
from aiogram.filters.command import Command


myinfo_router = Router()
@myinfo_router.message(Command("myinfo"))
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
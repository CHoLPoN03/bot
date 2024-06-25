from aiogram import Router, types
from aiogram.filters import Command
from crawler.housekg import get_page, get_links

house_router = Router()

@house_router.message(Command("obyavlenia"))
async def show_obyavlenia(message: types.Message):
    await message.answer("https://www.house.kg/details/4793335f896ed8e4d1f4-26541312")

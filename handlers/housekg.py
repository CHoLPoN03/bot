from aiogram import Router, types
from aiogram.filters import Command
from crawler.housekg import get_page, get_links


house_router = Router()

MAIN_URL = "https://www.house.kg/snyat"
@house_router.message(Command("obyavlenia"))
async def show_obyavlenia(message: types.Message):
    page = await get_page(MAIN_URL)
    links = get_links(page)
    for link in links:
        await message.answer(link)

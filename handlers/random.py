from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
import random
from pathlib import Path
import logging


random_pic_router = Router()
@random_pic_router.message(Command("random"))
async def random_pic_handler(message: types.Message):
    file_name = random.choice(list((Path(__file__).parent.parent / "Images").iterdir()))
    file_path = Path(__file__).parent.parent / "Images" / file_name
    logging.info(file_path)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)
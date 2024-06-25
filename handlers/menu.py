from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import database

menu_category_router = Router()

@menu_category_router.message(Command("menu_category"))
async def show_menu_category(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Пицца"), KeyboardButton(text="Десерты")],
            [KeyboardButton(text="Коктейли"), KeyboardButton(text="Напитки")],
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите категорию меню", reply_markup=kb)

category = ("пицца", "десерты", "коктейли", "напитки")


@menu_category_router.message(F.text.lower().in_(category))
async def show_dishes(message: types.Message):
     kb = ReplyKeyboardRemove()
     category = message.text.capitalize()
     dishes = await database.fetch("""
            SELECT * FROM dishes 
            INNER JOIN categories ON dishes.category_id = categories.id
            WHERE categories.name = ?
     """, (category, ))
     print(dishes)

     await message.answer(f"Блюда из категории {category}", reply_markup=kb)
     for dish in dishes:
         await message.answer(f"{dish['name']} - {dish['price']} сом")



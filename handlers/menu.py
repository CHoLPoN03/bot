from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import sqlite3

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

categories = ("пицца", "десерты", "коктейли", "напитки")


@menu_category_router.message(F.text.lower().in_(categories))
async def show_dishes(message: types.Message):
     kb = ReplyKeyboardRemove()
     categories = message.text
     connection = sqlite3.connect("db1.sqlite3")
     cursor = connection.cursor()
     query = cursor.execute("SELECT * FROM DISHES WHERE category_id = 2")
     dishes = query.fetchall()
     print(dishes)
     await message.answer("Блюда из категории ", reply_markup=kb)

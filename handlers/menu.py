from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

menu_category_router = Router()

@menu_category_router.message(Command("menu_category"))
async def show_menu_category(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Комбо")],
            [KeyboardButton(text="Десерты"), KeyboardButton(text="Коктейл")],
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите категорию меню", reply_markup=kb)

@menu_category_router.message(F.text == "Комбо")
async def show_combo(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer(" 2 пиццы -  Парочка что надо. 2 средние пиццы. "
                         "Цена комбо зависит от выбранных пицц и может быть увеличена"
                         "В комбо входит Пепперони и  - 1195 сом"
                         "\nДодо Микс -  "
                         "3 пиццы - Три удовольствия в нашем меню - это три средние пиццы на ваш выбор. "
                         "Цена комбо зависит от выбранных пицц и может быть увеличена - 1745 сом ", reply_markup=kb)

@menu_category_router.message(F.text == "Десерты")
async def show_desserts(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Пончик клубничный - Нежный пончик с клубничной начинкой"
                         " и разноцветной посыпкой "
                        "\nПончик Три шоколада - Нежный пончик с шоколадной начинкой,"
                         " глазурью и посыпкой", reply_markup=kb)

@menu_category_router.message(F.text == "Коктейл")
async def show_cocktail(message: types.Message):
    kb = ReplyKeyboardRemove()
    await message.answer("Молочный коктейль с печеньем Орео "
                         "Как вкуснее есть печенье? Его лучше пить! Попробуйте молочный коктейль с "
                         "мороженым и дробленым печеньем «Орео»"
                         "\nКлассический молочный коктейль = В мире так много коктейлей, "
                         "но классика — вечна. Попробуйте наш молочный напиток с мороженым"
                         , reply_markup=kb)

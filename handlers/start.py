from aiogram import Router, types, F
from aiogram.filters.command import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    # print("Message", message)
    # print("User info", message.from_user)

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(
                text="Наш сайт",
                url="https://dodopizza.kg/"
            )],
            [
                types.InlineKeyboardButton(
                    text="Инстаграм профиль",
                    url="https://www.instagram.com/dodopizzakg/?hl=ru"
                ),
                types.InlineKeyboardButton(
                    text="Контакты",
                    callback_data="contacts"
                ),
            ],
            [
                types.InlineKeyboardButton(
                    text="Инстаграм профиль",
                    url="https://www.instagram.com/dodopizzakg/?hl=ru"
                ),
            ],
            [types.InlineKeyboardButton(
                text="Меню",
                callback_data="menu"
            )],
            [
                types.InlineKeyboardButton(
                    text="О нас",
                    callback_data="about"
                )
            ],
        ]
    )

    name = message.from_user.first_name
    await message.answer(f"Добро пожаловать, {name}", reply_markup=kb)


@start_router.callback_query(F.data == "about")
async def about_handler(callback: types.CallbackQuery):
    await callback.message.answer("Мы - лучшее заведение в городе!")


@start_router.callback_query(F.data == "contacts")
async def contacts_handler(callback: types.CallbackQuery):
    contacts = """Контакты:
0(312) 550 550
0(551) 550 550
0(709) 550 550"""
    await callback.message.answer(contacts)


@start_router.callback_query(F.data == "menu")
async def menu_handler(callback: types.CallbackQuery):
    menu = """Меню Dodo pizza:
1. Сырная - Моцарелла, смесь сыров чеддер и пармезан, соус альфредо - от 295 сом
2. Баварская - Охотничьи колбаски, маринованные огурчики, красный лук, томаты, горчичный соус, моцарелла, томатный соус - от 735 сом
3. Маргарита - Увеличенная порция моцареллы, томаты, итальянские травы , томатный соус - от 565 сом"""
    await callback.message.answer(menu)




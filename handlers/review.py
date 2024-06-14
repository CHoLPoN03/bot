from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

review_router = Router()

# FSM - Finite State Machine - конечный автомат
class BookSurvey(StatesGroup):
    name = State()  # имя
    number = State()  # номер или инстаграм
    date = State()  # дата
    food = State()  # еда
    cleanliness = State()  # чистота
    comment = State()  # комментарий

@review_router.message(Command("review"))
async def start_review(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.name)  # устанавливаем состояние
    await message.answer("Как Вас зовут?")

@review_router.message(Command("stop"))
@review_router.message(F.text == "стоп")
async def stop_opros(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо! Ваш опрос закончен.")

@review_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookSurvey.number)
    await message.answer("Ваш номер телефона или оставьте ваш инстаграм")

@review_router.message(BookSurvey.number)
async def process_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    await state.set_state(BookSurvey.date)
    await message.answer("Дата вашего посещения нашего заведения (в формате ДД.ММ.ГГГГ)")

@review_router.message(BookSurvey.date)
async def process_date(message: types.Message, state: FSMContext):
    try:
        # Удаление лишних пробелов и кавычек
        date_text = message.text.strip().strip('"')
        # Проверка формата даты
        date = datetime.strptime(date_text, "%d.%m.%Y")
        await state.update_data(date=date_text)
        print("Дата введена корректно:", date_text)

        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3"), KeyboardButton(text="4"), KeyboardButton(text="5")]
            ],
            resize_keyboard=True
        )
        await state.set_state(BookSurvey.food)
        await message.answer("Как оцениваете качество еды?", reply_markup=keyboard)
        print("Состояние установлено на food")
    except ValueError as e:
        print("Ошибка:", e)
        await message.answer("Пожалуйста, введите дату в формате ДД.ММ.ГГГГ")

@review_router.message(BookSurvey.food)
async def process_food(message: types.Message, state: FSMContext):
    if message.text not in ["1", "2", "3", "4", "5"]:
        await message.answer("Пожалуйста, выберите значение от 1 до 5")
        return
    await state.update_data(food=message.text)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3"), KeyboardButton(text="4"), KeyboardButton(text="5")]
        ],
        resize_keyboard=True
    )
    await state.set_state(BookSurvey.cleanliness)
    await message.answer("Как оцениваете чистоту заведения?", reply_markup=keyboard)

@review_router.message(BookSurvey.cleanliness)
async def process_cleanliness(message: types.Message, state: FSMContext):
    if message.text not in ["1", "2", "3", "4", "5"]:
        await message.answer("Пожалуйста, выберите значение от 1 до 5")
        return
    await state.update_data(cleanliness=message.text)

    await state.set_state(BookSurvey.comment)
    await message.answer("Ваши дополнительные комментарии", reply_markup=ReplyKeyboardRemove())

@review_router.message(BookSurvey.comment)
async def process_comment(message: types.Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer(f"Спасибо за отзыв!\n\n"
                         f"Имя: {data.get('name')}\n"
                         f"Номер телефона/Instagram: {data.get('number')}\n"
                         f"Дата посещения: {data.get('date')}\n"
                         f"Качество еды: {data.get('food')}\n"
                         f"Чистота заведения: {data.get('cleanliness')}\n"
                         f"Комментарии: {data.get('comment')}")
    await message.answer("Спасибо за отзыв!")





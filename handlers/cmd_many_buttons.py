from aiogram.types import Message
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

async def cmd_many_buttons(message: Message):
    """
    Показывает 20 кнопока с цифрами по 5 штук в ряд by ReplyKeyboardBuilder
    :param message:
    :return:
    """
    kb = ReplyKeyboardBuilder()
    for i in range(1, 21):
        kb.add(KeyboardButton(text=str(i)))
    kb.adjust(5)
    await message.answer("Выберите цифру:", reply_markup=kb.as_markup(resize_keyboard=True))

async def cmd_by_row_buttons(message: Message):
    kb = ReplyKeyboardBuilder()
    kb.row(KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3"))
    kb.row(KeyboardButton(text="4"), KeyboardButton(text="5"))
    kb.row(KeyboardButton(text="6"), KeyboardButton(text="7"), KeyboardButton(text="8"))
    await message.answer("Выберите цифру:", reply_markup=kb.as_markup(resize_keyboard=True))



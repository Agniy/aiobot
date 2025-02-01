from random import randint

from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

async def cmd_inline_buttons(message: Message):
    """
    Показывает 20 кнопока с цифрами по 5 штук в ряд by InlineKeyboardBuilder
    :param message:
    :return:
    """
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="DevDao", url="https://dev-dao.ru/"))
    kb.row(InlineKeyboardButton(text="DevDao", url="https://dev-dao.ru/blog/28/"))

    await message.answer("Select link:", reply_markup=kb.as_markup())

async def cmd_random_number(message: Message):
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="Random number", callback_data=f"random_number"))
    await message.answer("Select number:", reply_markup=kb.as_markup())

async def cmd_random_number_callback(callback: CallbackQuery):
    await callback.message.answer(f"Your random number is {randint(1, 100)}")
    await callback.answer(' ')
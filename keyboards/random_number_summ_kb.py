from aiogram.types import Message
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def random_number_summ_kb() -> InlineKeyboardBuilder:
    """
    Показывает 20 кнопока с цифрами по 5 штук в ряд by ReplyKeyboardBuilder
    :param message:
    :return:
    """
    kb = InlineKeyboardBuilder()
    for i in range(1, 5):
        kb.add(InlineKeyboardButton(text=str(i), callback_data=f"two_numbers_{i}"))
    kb.adjust(5)
    return kb
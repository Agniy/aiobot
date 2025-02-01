from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_how_are_you_kb() -> ReplyKeyboardMarkup:
    """
    Возвращает клавиатуру с кнопками "Хорошо" и "Плохо"
    :return:
    """
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Хорошо"),
                KeyboardButton(text="Плохо")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return kb
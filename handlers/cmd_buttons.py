from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

async def cmd_buttons(message: Message):
    """
    Показывает 3 кнопки с разными приветствиями и реакциями на них
    :param message:
    :return:
    """

    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="👋 Привет"),
                KeyboardButton(text="👋 Здравствуй"),
                KeyboardButton(text="👋 Добрый день")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer("Выберите приветствие:", reply_markup=kb)

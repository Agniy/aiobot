from aiogram import types

async def cmd_sticker(message: types.Message):
    await message.answer_sticker(
        sticker="CAACAgIAAxkBAAENoU5nlKuU7_gnxA1a-7H1SSwgYo5nugACdEoAAqwq4Ur3PIAgM2uiVTYE"
    )
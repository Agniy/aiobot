from aiogram import  types

async def cmd_location(message: types.Message):
    await message.answer_location(55.7522, 37.6156)
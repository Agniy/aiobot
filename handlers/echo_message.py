from aiogram import types

async def echo_message(msg: types.Message):
    await msg.answer(msg.text)

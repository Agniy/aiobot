from aiogram import  types,html
from aiogram.enums import ParseMode

async def cmd_start(message: types.Message):
    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML
    )
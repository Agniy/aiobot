from aiogram import types
from aiogram.enums import ParseMode

async def cmd_text(message: types.Message):
    await message.answer(
        "<i>Italic text</i>\n<b>Bold text</b>\n<u>Underlined text</u>",
        parse_mode=ParseMode.HTML
    )
    await message.answer(
        "||Spoiler||\n~Strikethrough~",
        parse_mode=ParseMode.MARKDOWN_V2
    )

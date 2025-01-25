from aiogram import types
from aiogram.enums import DiceEmoji

async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.BOWLING)

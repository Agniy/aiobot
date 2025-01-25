from aiogram import  types
from aiogram.types import FSInputFile
from config.settings import settings
from aiogram.utils.media_group import MediaGroupBuilder

async def cmd_group(message: types.Message):
    media_group = MediaGroupBuilder(caption="Гуси и свиньи")
    media_group.add_photo(
        FSInputFile(settings.STATIC_DIR / "gus.jpg"),
        caption="Гусь лапчатый"
    )
    media_group.add_photo(
        FSInputFile(settings.STATIC_DIR / "svin.jpg"),
        caption="Свин обыкновенный"
    )
    await message.answer_media_group(media_group.build())
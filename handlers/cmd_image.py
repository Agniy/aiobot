from aiogram import  types
from aiogram.types import FSInputFile
from config.settings import settings

async def cmd_image(message: types.Message):
    image_path = settings.STATIC_DIR / "gus.jpg"
    image_file = FSInputFile(image_path)
    await message.answer_photo(image_file)
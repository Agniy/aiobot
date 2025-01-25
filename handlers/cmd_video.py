from aiogram import  types
from aiogram.types import FSInputFile
from config.settings import settings

async def cmd_video(message: types.Message):
    video_path = settings.STATIC_DIR / "sprey.mp4"
    video_file = FSInputFile(video_path)
    await message.answer_video(video_file,caption="Гусь лапчатый")
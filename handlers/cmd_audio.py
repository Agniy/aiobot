from aiogram import  types
from aiogram.types import FSInputFile
from config.settings import settings

async def cmd_audio(message: types.Message):
    audio_path = settings.STATIC_DIR / "featApolloJane.mp3"
    audio_file = FSInputFile(audio_path)
    await message.answer_audio(audio_file,caption="Тум тум")
    await message.answer_voice(audio_file,caption="Тум тум")
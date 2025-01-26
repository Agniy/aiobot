from aiogram import Bot
from aiogram import  types
from config.settings import settings


class DownloadPhoto:
    def __init__(self,bot: Bot):
        self.bot: Bot = bot

    async def download_photo(self, message:types.Message):
        photo = message.photo[-1]
        file_info = await self.bot.get_file(photo.file_id)
        file_extension = file_info.file_path.split('.')[-1]
        file_id = file_info.file_id

        await self.bot.download(message.photo[-1], destination=settings.MEDIA_DIR / f"{file_id}.{file_extension}")
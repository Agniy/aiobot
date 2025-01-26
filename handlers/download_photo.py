from aiogram import Bot
from aiogram import  types
from config.settings import settings


class DownloadPhoto:
    def __init__(self,bot: Bot):
        self.bot: Bot = bot

    async def download_photo(self, message:types.Message):
        await self.bot.download(message.photo[-1])
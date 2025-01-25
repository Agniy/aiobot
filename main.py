import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command

from handlers import (
    cmd_start,
    cmd_test_args,
    cmd_text,
    cmd_sticker,
    cmd_dice,
    cmd_help,
    echo_message,
    cmd_image,
    cmd_video
)
from middleware import LoggingMiddleware

from api_token import TOKEN

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self):
        self.bot = Bot(token=TOKEN)
        self.dp = Dispatcher()
        self._setup_middleware()
        self._setup_handlers()

    def _setup_middleware(self):
        self.dp.update.middleware(LoggingMiddleware())

    def _setup_handlers(self):
        self.dp.message.register(cmd_start, Command("start"))
        self.dp.message.register(cmd_help, Command("help"))
        self.dp.message.register(cmd_test_args, Command("test_args"))
        self.dp.message.register(cmd_text, F.text, Command("text"))
        self.dp.message.register(cmd_sticker, Command("sticker"))
        self.dp.message.register(cmd_dice, Command("dice"))
        self.dp.message.register(cmd_image, Command("image"))
        self.dp.message.register(cmd_video, Command("video"))
        self.dp.message.register(echo_message)


    async def start(self):
        logger.info("Bot started")
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(self.bot)

def main():
    bot = TelegramBot()
    asyncio.run(bot.start())

if __name__ == "__main__":
    main()

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
    cmd_video,
    cmd_group,
    cmd_audio,
    cmd_file,
    cmd_location,
    cmd_buttons,
    cmd_many_buttons,
    cmd_by_row_buttons,
    cmd_inline_buttons,
    cmd_random_number,
    cmd_random_number_callback,
    DownloadPhoto,

    how_are_you_handler,
    random_number_summ_handler,
    magic_test_handler,
)
from middleware import LoggingMiddleware
from config.settings import settings

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self):
        self.bot = Bot(token=settings.TOKEN)
        self.dp = Dispatcher()
        self._setup_middleware()

        # set up handlers on the root level
        # self._setup_handlers()

        # set up handlers on the router level
        self._setup_routers()

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
        self.dp.message.register(cmd_group, Command("group"))
        self.dp.message.register(cmd_audio, Command("audio"))
        self.dp.message.register(cmd_file, Command("file"))
        self.dp.message.register(cmd_location, Command("location"))
        self.dp.message.register(cmd_buttons, Command("buttons"))
        self.dp.message.register(DownloadPhoto(self.bot).download_photo, F.photo)
        self.dp.message.register(cmd_many_buttons, Command("many_buttons"))
        self.dp.message.register(cmd_inline_buttons, Command("inline_buttons"))
        self.dp.message.register(cmd_by_row_buttons, Command("by_row_buttons"))

        self.dp.message.register(cmd_random_number, Command("random_number"))
        self.dp.callback_query.register(cmd_random_number_callback)

        self.dp.message.register(echo_message)

    def _setup_routers(self):
        self.dp.include_routers(how_are_you_handler.router)
        self.dp.include_router(random_number_summ_handler.router)
        self.dp.include_router(magic_test_handler.router)

    async def start(self):
        logger.info("Bot started")
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(self.bot)

def main():
    bot = TelegramBot()
    asyncio.run(bot.start())

if __name__ == "__main__":
    main()

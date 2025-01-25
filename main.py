import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.types import Update
from typing import Any, Awaitable, Callable
from api_token import TOKEN

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='bot_logs.log'
)

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any]
    ) -> Any:
        # Log the incoming update
        if event.message:
            logger.info(
                f"Update ID: {event.update_id} | "
                f"From: {event.message.from_user.id} | "
                f"Chat: {event.message.chat.id} | "
                f"Text: {event.message.text}"
            )
        return await handler(event, data)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Register middleware
dp.update.middleware(LoggingMiddleware())

TEST_OF_HELP = """
/start - Start
/help - Help
/test_args - Test args <name> <age> <city>
"""

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("test_args"))
async def cmd_test_args(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer("Вы не передали аргументы")
        return

    try:
        name, age, city = command.args.split(" ")
    except ValueError:
        await message.answer("Неверный формат аргументов. Используйте: /test_args <name> <age> <city>")
        return

    await message.answer(f"Ваше имя: {name}, Ваш возраст: {age}, Ваш город: {city}")

@dp.message(Command("help", prefix="/"))
async def cmd_help(message: types.Message):
    await message.reply(TEST_OF_HELP)

@dp.message()
async def echo_message(msg: types.Message):
    await msg.answer(msg.text)

async def main():
    logger.info("Bot started")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

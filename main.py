import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from api_token import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

TEST_OF_HELP = """
/start - Start
/help - Help
"""

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("help", prefix="/"))
async def cmd_help(message: types.Message):
    await message.reply(TEST_OF_HELP)

@dp.message()
async def echo_message(msg: types.Message):
    await msg.answer(msg.text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True) # drop old updates
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
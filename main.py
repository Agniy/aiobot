import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from api_token import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
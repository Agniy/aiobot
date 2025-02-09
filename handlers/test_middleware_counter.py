from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def test_middleware_counter(message: Message, counter: int):
    await message.answer(f'Counter: {counter}')
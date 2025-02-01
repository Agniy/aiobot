from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards.random_number_summ_kb import random_number_summ_kb

router = Router()

@router.message(Command("random_number_summ"))
async def random_number_summ_handler(message: Message):
    await message.answer("Select number:", reply_markup=random_number_summ_kb().as_markup())

@router.callback_query(F.data.startswith("two_numbers_"))
async def random_number_summ_callback(callback: CallbackQuery):
    await callback.message.answer(f"Doubled number {int(callback.data.split('_')[2]) * 2}")
    await callback.answer(' ')
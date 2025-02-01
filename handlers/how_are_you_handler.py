from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.how_are_you_kb import get_how_are_you_kb

router = Router()

@router.message(Command("how_are_you"))
async def how_are_you_handler(message: Message):
    await message.answer("Как дела?", reply_markup=get_how_are_you_kb())

@router.message(F.text == "Хорошо")
async def how_are_you_handler_good(message: Message):
    await message.answer("Я рад за тебя!", reply_markup=ReplyKeyboardRemove())

@router.message(F.text == "Плохо")
async def how_are_you_handler_bad(message: Message):
    await message.answer("Я рад, что ты с нами!", reply_markup=ReplyKeyboardRemove())
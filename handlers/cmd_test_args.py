from aiogram import types
from aiogram.filters.command import CommandObject

async def cmd_test_args(message: types.Message, command: CommandObject):
    if not command.args:
        await message.answer("Please provide arguments")
        return

    try:
        name, age, city = command.args.split()
        await message.answer(f"Name: {name}, Age: {age}, City: {city}")
    except ValueError:
        await message.answer("Invalid format. Use: /test_args <name> <age> <city>")

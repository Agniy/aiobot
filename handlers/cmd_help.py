from aiogram import types

COMMANDS_HELP = """
/start - Start
/help - Help
/test_args - Test args <name> <age> <city>
/text - Show formatted text examples
/sticker - Send sticker
/dice - Roll dice
"""

async def cmd_help(message: types.Message):
    await message.reply(COMMANDS_HELP)

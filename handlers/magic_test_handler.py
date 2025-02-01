from aiogram import Router, F
from aiogram.types import Message, PhotoSize
from aiogram.enums import MessageEntityType

router = Router()

# Filter messages that contain specific text
@router.message(F.text == "hello")
async def handle_hello(message: Message):
    await message.answer("Hi there!")

@router.message(F.entities[...].type == MessageEntityType.EMAIL)
async def test_magic_handler(message: Message):
    await message.answer("EMAIL detected!")

@router.message(F.photo[-1].as_("photo"))
async def test_magic_handler(message: Message, photo: PhotoSize):
    await message.answer(f"{photo.file_id} {photo.file_unique_id} {photo.width} {photo.height} {photo.file_size}")

# Filter messages by content type
@router.message(F.content_type == "photo")
async def handle_photo(message: Message):
    await message.answer("Nice photo!")

# Complex filters with logical operators
@router.message(F.text.startswith("/start") & F.from_user.id == 12345)
async def handle_admin_start(message: Message):
    await message.answer("Welcome admin!")

# Filter by message length
@router.message(F.text.len() > 100)
async def handle_long_message(message: Message):
    await message.answer("That's a long message!")

# Check if text contains specific words
@router.message(F.text.contains("python"))
async def handle_python_mention(message: Message):
    await message.answer("Python is awesome!")

# Multiple conditions with in operator
@router.message(F.text.lower().in_(["hi", "hello", "hey"]))
async def handle_greetings(message: Message):
    await message.answer("Hello!")

# Filter by message video
@router.message(F.video)
async def handle_video(message: Message):
    await message.answer("Nice video!")

# Filter by message voice
@router.message(F.voice)
async def handle_voice(message: Message):
    await message.answer("Nice voice!")

# Filter by message animation
@router.message(F.animation)
async def handle_animation(message: Message):
    await message.answer("Nice animation!")

# Filter by message document
@router.message(F.document)
async def handle_document(message: Message):
    await message.answer("Nice document!")

# Filter by message audio
@router.message(F.audio)
async def handle_audio(message: Message):
    await message.answer("Nice audio!")

# Filter by message sticker
@router.message(F.sticker)
async def handle_sticker(message: Message):
    await message.answer("Nice sticker!")

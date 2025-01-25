import aiofiles
from aiogram import  types
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from config.settings import settings

async def cmd_image(message: types.Message):
    image_path = settings.STATIC_DIR / "gus.jpg"
    image_file = FSInputFile(image_path)
    await message.answer_photo(image_file,caption="Гусь лапчатый")

    await message.answer_photo(
        URLInputFile("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4wvHlghvqqzJfcrSo5ApaTgXSHteMyJHEQQ&s"),
        caption="Принцесса"
    )

    with open(image_path, "rb") as f:
        image_bytes = f.read()
        await message.answer_photo(
            BufferedInputFile(image_bytes, filename="gus.jpg"),
            caption="Гусь лапчатый"
        )

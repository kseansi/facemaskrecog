from aiogram import types
from aiogram.types import ContentType, InputFile
import process as pr
from loader import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_photo(message: types.Message):
    await message.photo[-1].download('C:/Users/laisbel/PycharmProjects/facemaskrecog/content/image.jpg')


@dp.message_handler(text='/photo')
async def send_photo(message: types.Message):
    chat_id = message.from_user.id
    pr.worker()
    await dp.bot.send_photo(chat_id=chat_id, photo=InputFile('C:/Users/laisbel/PycharmProjects/facemaskrecog/content/test.jpg'))

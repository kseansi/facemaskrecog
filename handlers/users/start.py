from aiogram import types
from loader import dp

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer('Прикрепите фото')


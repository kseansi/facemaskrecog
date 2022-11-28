from aiogram import types
from loader import dp


@dp.message_handler(text='/work')
async def command_start(message: types.Message):
    await message.answer('Сам работай')

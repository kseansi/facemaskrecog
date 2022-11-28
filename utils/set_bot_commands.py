from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commans([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('work', 'Работа бота')
    ])

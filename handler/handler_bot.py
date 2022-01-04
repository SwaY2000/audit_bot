from aiogram import types, Dispatcher

from help_file import dp, bot

import sys
sys.path.append('/tg_bot_for_audit/')

async def command_start(message: types.Message):
    print('user start')
    await message.answer('Привет! Теперь я буду твоим синоптиком :)')

def register_handlers(dp: Dispatcher):
    try:
        dp.register_message_handler(command_start, commands='start')
    except Exception:
        print('ERROR')

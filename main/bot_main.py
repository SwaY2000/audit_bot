from aiogram.utils import executor

from admin import admin_part
from help.help_file import dp
from client import client_part

import sys
sys.path.append('/tg_bot_for_audit/')



async def on_startup(_):
    print('Bot connected')

admin_part.register_handlers_admin(dp)
client_part.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
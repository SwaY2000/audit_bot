from aiogram.utils import executor

from admin.admin_part import *
from help.help_file import dp
from client.client_part import *

import sys
sys.path.append('/tg_bot_for_audit/')



async def on_startup(_):
    print('Bot connected')

register_handlers_admin(dp)
register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
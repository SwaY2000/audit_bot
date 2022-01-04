from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import BOT_TOKEN

import sys
sys.path.append('/tg_bot_for_audit/')

print(BOT_TOKEN.BOT_TOKEN)

storage = MemoryStorage()

bot = Bot(BOT_TOKEN.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
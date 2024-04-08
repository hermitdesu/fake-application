"""
There are bot initialization and database package adding.
"""

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.core import settings

# Bot initialization.
bot = Bot(settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
bot_dispatcher = Dispatcher(storage=MemoryStorage())

from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data_base import sqlite_db

storage = MemoryStorage()
sqlite_db.sql_start()

TOKEN = config("TOKEN", default="ERROR")
print(TOKEN)
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = [704415431, ]
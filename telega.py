from aiogram import Bot, Dispatcher 
from aiogram.filters.command import Command
from dotenv import dotenv_values
import asyncio

config = dotenv_values()
bot = Bot(token=config["TOKEN"])
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message):
    await message.reply('Дай денег')


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
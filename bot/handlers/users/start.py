from aiogram import types
from aiogram.filters import CommandStart

from bot.loader import dp


@dp.message(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Alaykum.")


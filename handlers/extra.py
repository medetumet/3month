from aiogram import types, Dispatcher
from config import bot, ADMINS
import random


async def echo(message: types.Message):
    if message.text.startswith('game') and message.from_user.id in ADMINS:
        await bot.send_dice(message.chat.id, emoji=random.choice(['⚽️', '🏀', '🎰', '🎳', '🎯', '🎲']))
    elif message.text.isnumeric():
        await bot.send_message(message.chat.id, int(message.text) ** 2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)

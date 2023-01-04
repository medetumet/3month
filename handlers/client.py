from config import dp, bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.bot_db import sql_command_random
from handlers.parser import ParserNews

# @dp.message_handler(commands=['quiz'])
async def quiz1(message: types.Message):
    button1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup = InlineKeyboardMarkup().add(button1)
    await bot.send_poll(message.chat.id,
                        question='сколько областей в Кыргызстане?',
                        options=['6', '7', '8'],
                        type='quiz',
                        correct_option_id=1,
                        reply_markup=markup)


async def meme(message: types.Message):
    with open('media/meme.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='very funny')


async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, 'Должно быть ответом на сообщение!')


async def get_random_user(message: types.Message):
    await sql_command_random(message)

async def parser_news(message: types.Message):
    items = ParserNews.parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,
            text=f"{item['link']}\n\n"
                 f"{item['title']}\n\n"
                 f"{item['date']}\n"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(meme, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(parser_news, commands=['news'])

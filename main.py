from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['quiz'])
async def quiz1(message: types.Message):
    button1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup = InlineKeyboardMarkup().add(button1)
    await bot.send_poll(message.chat.id,
                        question='сколько областей в Кыргызстане?',
                        options=['6', '7', '8'],
                        type='quiz',
                        correct_option_id=1,
                        reply_markup=markup)


@dp.callback_query_handler(text='button_call_1')
async def quiz2(call: types.CallbackQuery):
    await bot.send_poll(call.message.chat.id,
                        question='сколько городов конституционного значения в КР?',
                        options=['1', '3', '2', '4'],
                        type='quiz',
                        correct_option_id=2)


@dp.message_handler(commands=['mem'])
async def meme(message: types.Message):
    with open('media/meme.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='very funny')


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await bot.send_message(message.chat.id, int(message.text) ** 2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

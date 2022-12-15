from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz2(call: types.CallbackQuery):
    button2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    markup = InlineKeyboardMarkup().add(button2)
    await bot.send_poll(call.message.chat.id,
                        question='сколько городов конституционного значения в КР?',
                        options=['1', '3', '2', '4'],
                        type='quiz',
                        correct_option_id=2,
                        reply_markup=markup)


async def quiz3(call: types.CallbackQuery):
    await bot.send_poll(call.message.chat.id,
                        question='День независимости КР?',
                        options=['31.08', '31.09', '30.08', '31.07'],
                        type='quiz',
                        correct_option_id=0)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, text='button_call_1')
    dp.register_callback_query_handler(quiz3, text='button_call_2')

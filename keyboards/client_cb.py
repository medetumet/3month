from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel_button = KeyboardButton("CANCEL")
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel_button)

backend = KeyboardButton("BackEnd")
frontend = KeyboardButton("FrontEnd")
android = KeyboardButton("Android")
ios = KeyboardButton("IOS")
ux_ui = KeyboardButton("UXUI")

direction_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(backend, frontend, android,
                                                                                         ios, ux_ui, cancel_button)
submit_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton("Да"), KeyboardButton("Нет")
)

from aiogram import types, Dispatcher
from config import bot
from config import ADMINS
from database.bot_db import sql_command_delete, sql_command_all
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не мой босс!")
    else:
        mentors = await sql_command_all()
        for mentor in mentors:
            await message.answer(
                f"id:{mentor[0]} name:{mentor[1]} direction{mentor[2]} "
                f"age:{mentor[3]} group:{mentor[4]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(f"delete {mentor[1]}",
                                         callback_data=f"delete {mentor[0]}")
                )
            )


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))

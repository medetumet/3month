from aiogram.utils import executor
from config import dp
from handlers import admin, callback, client, extra, fsmadminmentor
from database.bot_db import sql_create

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmadminmentor.register_handlers_fsm(dp)
extra.register_handlers_extra(dp)


async def on_startup(_):
    sql_create()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

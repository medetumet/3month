from aiogram.utils import executor
from config import dp
from handlers import admin, callback, client, extra, fsmadminmentor

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmadminmentor.register_handlers_fsm(dp)
extra.register_handlers_extra(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

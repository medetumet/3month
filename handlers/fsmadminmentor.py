from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboards import client_cb
from config import ADMINS


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    gruppa = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type != 'private':
        await bot.send_message(message.chat.id, 'Нельзя регестрировать в группе')
    else:
        if message.from_user.id in ADMINS:
            await FSMAdmin.id.set()
            await message.answer('ВВедите айди ментора', reply_markup=client_cb.cancel_markup)
        else:
            await message.answer('Ты не админ')


async def load_id(message: types.Message, state: FSMContext):
    try:
        id = int(message.text)
        async with state.proxy() as data:
            data['id'] = id
        await FSMAdmin.next()
        await message.answer('ВВедите имя ментора', reply_markup=client_cb.cancel_markup)
    except:
        await message.answer('Айди может быть только из цифр', reply_markup=client_cb.cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Выберите направление', reply_markup=client_cb.direction_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Введите возраст ментора!', reply_markup=client_cb.cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        async with state.proxy() as data:
            data['age'] = age
        await FSMAdmin.next()
        await message.answer("Введите группу ментора", reply_markup=client_cb.cancel_markup)
    except:
        await message.answer('Возраст может быть только числовой', reply_markup=client_cb.cancel_markup)


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gruppa'] = message.text
        await message.answer(
            f"ID:{data['id']}\nName:{data['name']}\n{data['direction']}\n{data['age']}\n{data['gruppa']}")
        await message.answer("Все правильно?", reply_markup=client_cb.submit_markup)
    await FSMAdmin.next()


async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        # запись в БД
        await message.answer('Супер!!')
    else:
        await message.answer('Ну и ладно')
    await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()
    if cur_state is not None:
        await state.finish()
        await message.answer('Отменено')


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, commands=['/cancel'], state='*')
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.gruppa)
    dp.register_message_handler(submit, state=FSMAdmin.submit)

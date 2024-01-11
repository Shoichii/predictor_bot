from aiogram import types
from bot.loader import dp
from bot.states import User_Data_Change
from bot.info.user_data import keyboard, data_button
from aiogram.dispatcher import FSMContext
import bot.django_crud as dj
import re

# отмена изменения имени
@dp.callback_query_handler(lambda call: call.data == 'cancel_change_data_button',
                        state=User_Data_Change)
async def cancel_change_data(call: types.CallbackQuery, state:FSMContext):
    await call.message.delete()
    await data_button(call.message, call.from_user.id)
    await state.finish()


# запрос нового имени
@dp.callback_query_handler(lambda call: call.data == 'change_name_button')
async def req_new_name(call: types.CallbackQuery):
    await call.message.delete()

    await call.message.answer('Напишите новое ФИО', reply_markup=keyboard)
    await User_Data_Change.name_change.set()


# запись нового имени
@dp.message_handler(state=User_Data_Change.name_change)
async def set_new_name(msg: types.Message, state:FSMContext):
    await dj.set_new_name(msg.from_user.id, msg.text)
    await dj.reset_base_numbers(msg.from_user.id)
    await data_button(msg, msg.from_user.id)
    await state.finish()


# запрос новой даты рождения
@dp.callback_query_handler(lambda call: call.data == 'change_birthday_button')
async def req_new_birthday(call: types.CallbackQuery):
    await call.message.delete()

    await call.message.answer('Напишите новую дату рождения в формате: 01.01.1970', reply_markup=keyboard)
    await User_Data_Change.birthday_change.set()


# запись новой даты рождения
@dp.message_handler(state=User_Data_Change.birthday_change)
async def set_new_birthday(msg: types.Message, state:FSMContext):
    date_regex = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
    match = date_regex.search(msg.text)
    if not match:
        await msg.answer('В сообщении должна быть только дата формата ХХ.ХХ.ХХХХ(пример: 01.01.1970)')
        return
    await dj.set_new_birthday(msg.from_user.id, msg.text)
    await dj.reset_base_numbers(msg.from_user.id)
    await data_button(msg, msg.from_user.id)
    await state.finish()
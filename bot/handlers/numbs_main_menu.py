from bot.loader import dp
from aiogram import types
from bot.info.main_numbs_menu import numerology_button
from bot.info.base_numbers_menu import numb_core
from bot.info.other_numbers import core_synthez
from bot.info.forecast_numbers import forecast
from bot.info.numerology_relationship import relationships
import bot.django_crud as dj

@dp.callback_query_handler(lambda call: call.data.endswith('_main_menu'))
async def main_menu_buttons_handle(call: types.CallbackQuery):
    await call.message.delete()
    if call.data.startswith('base_numbers'):
        await numb_core(call.message, call.from_user.id)
        await dj.set_stat(call.from_user.id, 'numerology_count')
    if call.data.startswith('other_numbers'):
        await core_synthez(call.message, call.from_user.id)
        await dj.set_stat(call.from_user.id, 'core_synthesis')
    if call.data.startswith('forecast_numbers'):
        await forecast(call.message, call.from_user.id)
        await dj.set_stat(call.from_user.id, 'forecast')
    if call.data.startswith('relationship_button'):
        await relationships(call.message)


# возврат в главное меню нумерологии
@dp.callback_query_handler(lambda call: call.data == 'back_to_main_menu_button')
async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.delete()
    await numerology_button(call.message, call.from_user.id)


# возврат в главное меню базовых чисел
@dp.callback_query_handler(lambda call: call.data == 'back_to_base_numbers_button')
async def open_base_numbers(call: types.CallbackQuery):
    await call.message.delete()
    await numb_core(call.message, call.from_user.id)

# возврат в главное меню синтеза ядра
@dp.callback_query_handler(lambda call: call.data == 'back_to_other_numbers_button')
async def open_other_numbers(call: types.CallbackQuery):
    await call.message.delete()
    await core_synthez(call.message, call.from_user.id)


# возврат в главное меню прогноза
@dp.callback_query_handler(lambda call: call.data == 'back_to_base_forecast_button')
async def open_forecast_numbers(call: types.CallbackQuery):
    await call.message.delete()
    await forecast(call.message, call.from_user.id)


# возврат в главное меню взаимоотношений
@dp.callback_query_handler(lambda call: call.data == 'back_to_relationships_button')
async def open_relationships(call: types.CallbackQuery):
    await call.message.delete()
    await relationships(call.message)
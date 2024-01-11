from bot.loader import dp, bot
from aiogram import types
from bot.info.bridges_numbers import get_bridges_numbers_button, message_text, info
from bot.info.other_numbers import back_to_other_numbers_button
from bot.utils import check_seals_amount, add_base_numbers_to_msg
import asyncio
from bot.prices import bridges_number_price
import os
from bot.states import Numbers
from aiogram.dispatcher import FSMContext
import bot.django_crud as dj


@dp.callback_query_handler(lambda call: call.data == 'bridges_numbers_button')
async def open_bridges_numbers(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = types.InlineKeyboardMarkup().add(get_bridges_numbers_button).add(back_to_other_numbers_button)
    base_numbers = await dj.get_base_numbers_data(call.from_user.id)
    message_data = await add_base_numbers_to_msg(message_text, base_numbers)
    await call.message.answer(message_data.get('message'), reply_markup=keyboard, parse_mode='HTML')


@dp.callback_query_handler(lambda call: call.data == 'get_bridges_numbers_button')
async def get_expression_number(call: types.CallbackQuery):
    await call.message.delete()
    is_seals_enough = await check_seals_amount(call.message, call.from_user.id, bridges_number_price)
    if not is_seals_enough:
        return
    base_numbers = await dj.get_base_numbers_data(call.from_user.id)
    message_data = await add_base_numbers_to_msg(message_text, base_numbers)
    if message_data.get('count') < 2:
        keyboard = types.InlineKeyboardMarkup().add(back_to_other_numbers_button)
        await call.message.answer('Вам известно менее 2х базовых чисел. Узнайте минимум 2 и возвращайтесь 😉',
                                reply_markup= keyboard)
        return
    await dj.minus_seals(call.from_user.id,bridges_number_price)
    await call.message.answer('👁👁👁Печати сорваны👁👁👁')
    base_numbers = await dj.get_base_numbers_data(call.from_user.id)
    message = 'Введите одно из чиссел из нумерологического ядра. Например Ваше число жизненного пути.\n\n'
    message = await add_base_numbers_to_msg(message, base_numbers)
    await call.message.answer(message)
    await Numbers.first_numb.set()


@dp.message_handler(state=Numbers.first_numb)
async def get_frist_number(msg: types.Message, state: FSMContext):
    if not msg.text.isdigit():
        await msg.answer('Необходимо ввести число')
        return
    elif 1 < int(msg.text) and int(msg.text) > 31:
        await msg.answer('Это должно быть число от 1 до 31')
        return
    await state.update_data(first_numb = int(msg.text))
    base_numbers = await dj.get_base_numbers_data(msg.from_user.id)
    message = 'Введите Ваше второе число из нумерологического ядра. Например, Ваше число экспресии.'
    message = await add_base_numbers_to_msg(message, base_numbers)
    await msg.answer(message)
    await Numbers.second_numb.set()
    
@dp.message_handler(state=Numbers.second_numb)
async def get_frist_number(msg: types.Message, state: FSMContext):
    if not msg.text.isdigit():
        await msg.answer('Необходимо ввести число')
        return
    elif 1 < int(msg.text) and int(msg.text) > 31:
        await msg.answer('Это должно быть число от 1 до 31')
        return
    state_data = await state.get_data()
    first_numb = state_data.get('first_numb')
    second_numb = int(msg.text)
    
    if first_numb == 11 or first_numb == 22 or first_numb == 33:
        digits = [int(digit) for digit in str(first_numb)]
        first_numb = sum(digits)
    
    if second_numb == 11 or second_numb == 22 or second_numb == 33:
        digits = [int(digit) for digit in str(second_numb)]
        second_numb = sum(digits)
    
    if first_numb > second_numb:
        bridges_number = first_numb - second_numb
    else:
        bridges_number = second_numb - first_numb
    
    
    img = info[str(bridges_number)]['img']
    value = info[str(bridges_number)]['value']
    
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'bot', 'imgs', 'bridges_numbers', img)
    with open(file_path, 'rb') as photo:
        file = types.InputFile(photo)
        await msg.answer_photo(photo=file, caption=value)
        keyboard = types.InlineKeyboardMarkup().add(back_to_other_numbers_button)
        await msg.answer('1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣\nК другим числам!', reply_markup=keyboard)
    await state.finish()
from bot.loader import dp, bot
from aiogram import types
from bot.info.realization_number import message_text,get_realization_numbers_button , info
from bot.info.other_numbers import back_to_other_numbers_button
import asyncio
import bot.django_crud as dj
import os
from bot.prices import realization_number_price
from bot.utils import check_seals_amount


@dp.callback_query_handler(lambda call: call.data == 'realization_numbers_button')
async def open_realization_numbers(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = types.InlineKeyboardMarkup().add(get_realization_numbers_button).add(back_to_other_numbers_button)
    await call.message.answer(message_text, reply_markup=keyboard, parse_mode='HTML')


@dp.callback_query_handler(lambda call: call.data == 'get_realization_numbers_button')
async def get_realization_numbers(call: types.CallbackQuery):
    await call.message.delete()
    is_seals_enough = await check_seals_amount(call.message, call.from_user.id, realization_number_price)
    if not is_seals_enough:
        return
    
    await dj.minus_seals(call.from_user.id,realization_number_price)
    base_number = await dj.get_base_numbers_data(call.from_user.id)
    keyboard = types.InlineKeyboardMarkup().add(back_to_other_numbers_button)
    error_message = 'Чтобы открыть это число нужно знать число жизненного пути и число экспрессии. '
    life_path_number = base_number.life_path_number
    expression_number = base_number.expression_number
    if(life_path_number == None or expression_number == None):
        error_message += error_message + 'У вас не открыты оба эти числа.'
        await call.message.answer(error_message, reply_markup=keyboard)
        return
    if(life_path_number == None):
        error_message += error_message + 'У вас не открыто число жизненного пути.'
        await call.message.answer(error_message, reply_markup=keyboard)
        return
    if(expression_number == None):
        error_message += error_message + 'У вас не открыто число экспрессии.'
        await call.message.answer(error_message, reply_markup=keyboard)
        return
    realization_number = life_path_number + expression_number
    if realization_number != 11 or realization_number != 22 or realization_number != 33:
        while realization_number not in range(0,10):
            number_sum = 0
            for numb in str(realization_number):
                number_sum += int(numb)
            realization_number = number_sum
    
    realization_number = str(realization_number)
    img = info[realization_number]['img']
    value = info[realization_number]['value']
    
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'bot', 'imgs', 'realization_numbers', img)
    with open(file_path, 'rb') as photo:
        file = types.InputFile(photo)
        await call.message.answer('👁👁👁Печати сорваны👁👁👁')
        await asyncio.sleep(0.3)
        await call.message.answer_photo(photo=file, caption=value)
        await call.message.answer('1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣\nК другим числам!', reply_markup=keyboard)
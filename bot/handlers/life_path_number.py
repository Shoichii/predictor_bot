from bot.loader import dp, bot
from aiogram import types
from bot.info.life_path_number import message_text,get_life_path_number_button, info
from bot.info.base_numbers_menu import back_to_base_numbers_button
import asyncio
import bot.django_crud as dj
import os
from bot.prices import life_path_numbers_price
from bot.utils import check_seals_amount


@dp.callback_query_handler(lambda call: call.data == 'life_path_numbers_button')
async def open_life_path_numbers_menu(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = types.InlineKeyboardMarkup().add(get_life_path_number_button).add(back_to_base_numbers_button)
    await call.message.answer(message_text, reply_markup=keyboard, parse_mode='HTML')


@dp.callback_query_handler(lambda call: call.data == 'get_life_path_number_button')
async def get_life_path_number(call: types.CallbackQuery):
    await call.message.delete()
    is_seals_enough = await check_seals_amount(call.message, call.from_user.id, life_path_numbers_price)
    if not is_seals_enough:
        return
    
    await dj.minus_seals(call.from_user.id,life_path_numbers_price)
    life_path_number = await dj.life_path_number_handler(call.from_user.id)
    life_path_number = str(life_path_number)
    img = info[life_path_number]['img']
    value = info[life_path_number]['value']
    
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'bot', 'imgs', 'life_path_numbers', img)
    with open(file_path, 'rb') as photo:
        file = types.InputFile(photo)
        await call.message.answer('👁👁👁Печати сорваны👁👁👁')
        await asyncio.sleep(0.3)
        keyboard = types.InlineKeyboardMarkup().add(back_to_base_numbers_button)
        await call.message.answer_photo(photo=file, caption=value)
        await call.message.answer('1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣\nК другим числам!', reply_markup=keyboard)
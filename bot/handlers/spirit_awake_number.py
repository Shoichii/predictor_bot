from bot.loader import dp, bot
from aiogram import types
from bot.info.spirit_awake_number import message_text, get_spirit_awake_numbers_button, info
from bot.info.base_numbers_menu import back_to_base_numbers_button
import asyncio
import bot.django_crud as dj
import os
from bot.prices import spirit_awake_numbers_price
from bot.utils import check_seals_amount


@dp.callback_query_handler(lambda call: call.data == 'spirit_awake_numbers_button')
async def open_spirit_awake_number(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = types.InlineKeyboardMarkup().add(get_spirit_awake_numbers_button).add(back_to_base_numbers_button)
    await call.message.answer(message_text, reply_markup=keyboard, parse_mode='HTML')


@dp.callback_query_handler(lambda call: call.data == 'get_spirit_awake_numbers_button')
async def get_spirit_awake_number(call: types.CallbackQuery):
    await call.message.delete()
    is_seals_enough = await check_seals_amount(call.message, call.from_user.id, spirit_awake_numbers_price)
    if not is_seals_enough:
        return
    
    await dj.minus_seals(call.from_user.id, spirit_awake_numbers_price)
    spirit_awake_number = await dj.spirit_awake_number_handler(call.from_user.id)
    spirit_awake_number = str(spirit_awake_number)
    img = info[spirit_awake_number]['img']
    value = info[spirit_awake_number]['value']
    
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'bot', 'imgs', 'spirit_awake_numbers', img)
    with open(file_path, 'rb') as photo:
        file = types.InputFile(photo)
        await call.message.answer('👁👁👁Печати сорваны👁👁👁')
        await asyncio.sleep(0.3)
        keyboard = types.InlineKeyboardMarkup().add(back_to_base_numbers_button)
        await call.message.answer_photo(photo=file, caption=value)
        await call.message.answer('1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣\nК другим числам!', reply_markup=keyboard)
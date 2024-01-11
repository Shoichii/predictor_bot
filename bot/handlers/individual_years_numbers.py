from bot.loader import dp, bot
from aiogram import types
from bot.info.individual_years_numbers import get_individual_years_numbers_button, message_text, info
from bot.info.forecast_numbers import back_to_base_forecast_button
from bot.utils import check_seals_amount
from bot.prices import individual_years_number_price
import os
from bot.states import Numbers
from aiogram.dispatcher import FSMContext
import bot.django_crud as dj

@dp.callback_query_handler(lambda call: call.data == 'individual_years_numbers_button')
async def open_individual_years_number(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = types.InlineKeyboardMarkup().add(get_individual_years_numbers_button).add(back_to_base_forecast_button)
    await call.message.answer(message_text, reply_markup=keyboard, parse_mode='HTML')
    
@dp.callback_query_handler(lambda call: call.data == 'get_individual_years_numbers_button')
async def get_individual_years_number(call: types.CallbackQuery):
    await call.message.delete()
    is_seals_enough = await check_seals_amount(call.message, call.from_user.id, individual_years_number_price)
    if not is_seals_enough:
        return
    
    await dj.minus_seals(call.from_user.id,individual_years_number_price)
    await call.message.answer('👁👁👁Печати сорваны👁👁👁')
    await call.message.answer('Введите интересующий Вас год. Например: 1992')
    await Numbers.individual_year.set()
    
    
    
@dp.message_handler(state=Numbers.individual_year)
async def get_frist_number(msg: types.Message, state: FSMContext):
    if not msg.text.isdigit():
        await msg.answer('Необходимо ввести число')
        return
    
    user = await dj.get_user_data(msg.from_user.id)
    birthday = user.birthday.strftime("%d.%m.%Y")
    day = int(birthday.split('.')[0])
    month = int(birthday.split('.')[1])
    
    calc_day = day
    if calc_day != 11 or calc_day != 22:
        while calc_day not in range(0,10):
            number_sum = 0
            for numb in str(calc_day):
                number_sum += int(numb)
            calc_day = number_sum
    
    calc_month = month
    if calc_month != 11:
        while calc_month not in range(0,10):
            number_sum = 0
            for numb in str(calc_month):
                number_sum += int(numb)
            calc_month = number_sum
        
    calc_year = int(msg.text)
    if calc_year != 11 or calc_year != 22 or calc_year != 33:
        while calc_year not in range(0,10):
            number_sum = 0
            for numb in str(calc_year):
                number_sum += int(numb)
            calc_year = number_sum
        
    individual_year = calc_day + calc_month + calc_year
    while individual_year not in range(0,10):
        number_sum = 0
        for numb in str(individual_year):
            number_sum += int(numb)
        individual_year = number_sum

    individual_year_number = str(individual_year)
    
    img = info[individual_year_number]['img']
    value = info[individual_year_number]['value']
    
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'bot', 'imgs', 'individual_years_numbers', img)
    with open(file_path, 'rb') as photo:
        file = types.InputFile(photo)
        await msg.answer_photo(photo=file, caption=value)
        keyboard = types.InlineKeyboardMarkup().add(back_to_base_forecast_button)
        await msg.answer('1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣\nК другим числам!', reply_markup=keyboard)
    await state.finish()
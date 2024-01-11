from bot.loader import dp, bot
from aiogram import types
from bot.info.test_numbers import message_text, get_test_numbers_button, info
from bot.info.forecast_numbers import back_to_base_forecast_button
import asyncio
import bot.django_crud as dj
import os
from bot.prices import test_number_price
from bot.utils import check_seals_amount


@dp.callback_query_handler(lambda call: call.data == 'test_numbers_button')
async def open_test_number(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = types.InlineKeyboardMarkup().add(get_test_numbers_button).add(back_to_base_forecast_button)
    await call.message.answer(message_text, reply_markup=keyboard, parse_mode='HTML')


@dp.callback_query_handler(lambda call: call.data == 'get_test_numbers_button')
async def get_test_number(call: types.CallbackQuery):
    await call.message.delete()
    is_seals_enough = await check_seals_amount(call.message, call.from_user.id, test_number_price)
    if not is_seals_enough:
        return
    
    await dj.minus_seals(call.from_user.id, test_number_price)
    user = await dj.get_user_data(call.from_user.id)
    birthday = user.birthday.strftime("%d.%m.%Y")
    day = int(birthday.split('.')[0])
    month = int(birthday.split('.')[1])
    year = int(birthday.split('.')[2])
    
    tests = []

    calc_day = day
    while calc_day not in range(0,10):
        number_sum = 0
        for numb in str(calc_day):
            number_sum += int(numb)
        calc_day = number_sum
        
    calc_month = month
    while calc_month not in range(0,10):
        number_sum = 0
        for numb in str(calc_month):
            number_sum += int(numb)
        calc_month = number_sum
        
    calc_year = year
    while calc_year not in range(0,10):
        number_sum = 0
        for numb in str(calc_year):
            number_sum += int(numb)
        calc_year = number_sum
        
    #первое испытание
    if calc_day > calc_month:
        first_test = calc_day - calc_month
    else:
        first_test = calc_month - calc_day
    tests.append(first_test)

    #второе испытание
    if calc_day > calc_year:
        second_test = calc_day - calc_year
    else:
        second_test = calc_year - calc_day
    tests.append(second_test)
    
    #третье испытание
    if first_test > second_test:
        third_test = first_test - second_test
    else:
        third_test = second_test - first_test
    tests.append(third_test)

    #четвёртое испытание
    if calc_month > calc_year:
        fourth_test = calc_month - calc_year
    else:
        fourth_test = calc_year - calc_month
    tests.append(fourth_test)

    test_titles = ['<b>Первое испытание\n\n</b>', '<b>Второе испытание\n\n</b>',
                    '<b>Третье испытание\n\n</b>', '<b>Четвёртое испытание\n\n</b>']
    await call.message.answer('👁👁👁Печати сорваны👁👁👁')
    for i, test in enumerate(tests):
        test = str(test)
        img = info[test]['img']
        value = info[test]['value']
        value = test_titles[i] + value
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, 'bot', 'imgs', 'test_numbers', img)
        with open(file_path, 'rb') as photo:
            file = types.InputFile(photo)
            await asyncio.sleep(0.3)
            await call.message.answer_photo(photo=file, caption=value)
    keyboard = types.InlineKeyboardMarkup().add(back_to_base_forecast_button)
    await call.message.answer('1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣\nК другим числам!', reply_markup=keyboard)
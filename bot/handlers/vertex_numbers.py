from bot.loader import dp, bot
from aiogram import types
from bot.info.vertex_numbers import message_text, get_vertex_numbers_button, info
from bot.info.forecast_numbers import back_to_base_forecast_button
import asyncio
import bot.django_crud as dj
import os
from bot.prices import vertex_number_price
from bot.utils import check_seals_amount


@dp.callback_query_handler(lambda call: call.data == 'vertex_numbers_button')
async def open_vertex_number(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = types.InlineKeyboardMarkup().add(get_vertex_numbers_button).add(back_to_base_forecast_button)
    await call.message.answer(message_text, reply_markup=keyboard, parse_mode='HTML')


@dp.callback_query_handler(lambda call: call.data == 'get_vertex_numbers_button')
async def get_vertex_number(call: types.CallbackQuery):
    await call.message.delete()
    is_seals_enough = await check_seals_amount(call.message, call.from_user.id, vertex_number_price)
    if not is_seals_enough:
        return
    
    await dj.minus_seals(call.from_user.id, vertex_number_price)
    user = await dj.get_user_data(call.from_user.id)
    birthday = user.birthday.strftime("%d.%m.%Y")
    day = int(birthday.split('.')[0])
    month = int(birthday.split('.')[1])
    year = int(birthday.split('.')[2])
    
    vertexes = []

    #первая вершина
    first_vertex = day + month
    if first_vertex != 11 or first_vertex != 22 or first_vertex != 33:
        while first_vertex not in range(0,10):
            number_sum = 0
            for numb in str(first_vertex):
                number_sum += int(numb)
            first_vertex = number_sum
    vertexes.append(first_vertex)

    #вторая вершина
    calc_day = day
    if calc_day != 11 or calc_day != 22 or calc_day != 33:
        while calc_day not in range(0,10):
            number_sum = 0
            for numb in str(calc_day):
                number_sum += int(numb)
            calc_day = number_sum
    
    calc_year = year
    if calc_year != 11 or calc_year != 22 or calc_year != 33:
        while calc_year not in range(0,10):
            number_sum = 0
            for numb in str(calc_year):
                number_sum += int(numb)
            calc_year = number_sum
    
    second_vertex = calc_day + calc_year
    if second_vertex != 11 or second_vertex != 22 or second_vertex != 33:
        while second_vertex not in range(0,10):
            number_sum = 0
            for numb in str(second_vertex):
                number_sum += int(numb)
            second_vertex = number_sum
    vertexes.append(second_vertex)

    # третья вершина
    third_vertex = first_vertex + second_vertex
    if third_vertex != 11 or third_vertex != 22 or third_vertex != 33:
        while third_vertex not in range(0,10):
            number_sum = 0
            for numb in str(third_vertex):
                number_sum += int(numb)
            third_vertex = number_sum
    vertexes.append(third_vertex)

    # четвёртая вершина
    calc_month = month
    if calc_month != 11:
        while calc_month not in range(0,10):
            number_sum = 0
            for numb in str(calc_month):
                number_sum += int(numb)
            calc_month = number_sum
    
    fourth_vertex = calc_month + calc_year
    if fourth_vertex != 11 or fourth_vertex != 22 or fourth_vertex != 33:
        while fourth_vertex not in range(0,10):
            number_sum = 0
            for numb in str(fourth_vertex):
                number_sum += int(numb)
            fourth_vertex = number_sum

    vertexes.append(fourth_vertex)
    
    vertex_titles = ['<b>Первая вершина\n\n</b>', '<b>Вторая вершина\n\n</b>',
                    '<b>Третья вершина\n\n</b>', '<b>Четвёртая вершина\n\n</b>']
    await call.message.answer('👁👁👁Печати сорваны👁👁👁')
    for i, vertex in enumerate(vertexes):
        vertex = str(vertex)
        img = info[vertex]['img']
        value = info[vertex]['value']
        value = vertex_titles[i] + value
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, 'bot', 'imgs', 'vertex_numbers', img)
        with open(file_path, 'rb') as photo:
            file = types.InputFile(photo)
            await asyncio.sleep(0.3)
            await call.message.answer_photo(photo=file, caption=value)
    keyboard = types.InlineKeyboardMarkup().add(back_to_base_forecast_button)
    await call.message.answer('1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣\nК другим числам!', reply_markup=keyboard)
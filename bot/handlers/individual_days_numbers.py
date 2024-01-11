from bot.loader import dp, bot
from aiogram import types
from bot.info.individual_days_numbers import get_individual_days_numbers_button, message_text, info
from bot.info.forecast_numbers import back_to_base_forecast_button
from bot.utils import check_seals_amount
from bot.prices import individual_days_number_price
import os
from bot.states import Numbers
from aiogram.dispatcher import FSMContext
import bot.django_crud as dj


@dp.callback_query_handler(lambda call: call.data == 'individual_days_numbers_button')
async def open_individual_days_number(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = types.InlineKeyboardMarkup().add(get_individual_days_numbers_button).add(back_to_base_forecast_button)
    await call.message.answer(message_text, reply_markup=keyboard, parse_mode='HTML')
    
@dp.callback_query_handler(lambda call: call.data == 'get_individual_days_numbers_button')
async def get_individual_days_number(call: types.CallbackQuery):
    await call.message.delete()
    is_seals_enough = await check_seals_amount(call.message, call.from_user.id, individual_days_number_price)
    if not is_seals_enough:
        return
    
    await dj.minus_seals(call.from_user.id,individual_days_number_price)
    await call.message.answer('👁👁👁Печати сорваны👁👁👁')
    await call.message.answer('Введите число Вашего индивидуального месяца от 1 до 9. Например: 7.')
    await Numbers.individual_day_month.set()
    
@dp.message_handler(state=Numbers.individual_day_month)
async def get_frist_number(msg: types.Message, state: FSMContext):
    if not msg.text.isdigit():
        await msg.answer('Необходимо ввести число')
        return
    elif int(msg.text) > 9 or int(msg.text) == 0:
        await msg.answer('Это должно быть число от 1 до 9.')
        return
    await state.update_data(individual_day_month = int(msg.text))
    await msg.answer('Введите номер дня, о котором желаете узнать. Например: 15.')
    await Numbers.individual_day_day.set()

    
@dp.message_handler(state=Numbers.individual_day_day)
async def get_second_number(msg: types.Message, state: FSMContext):
    if not msg.text.isdigit():
        await msg.answer('Необходимо ввести число')
        return
    elif int(msg.text) > 31 or int(msg.text) == 0:
        await msg.answer('Это должно быть число от 1 до 31.')
        return
    state_data = await state.get_data()
    month = state_data.get('individual_day_month')
    day = int(msg.text)
    calc_day = day
    if calc_day != 11:
        while calc_day not in range(0,10):
            number_sum = 0
            for numb in str(calc_day):
                number_sum += int(numb)
            calc_day = number_sum
            
    individual_day = calc_day + month
    while individual_day not in range(0,10):
        number_sum = 0
        for numb in str(individual_day):
            number_sum += int(numb)
        individual_day = number_sum

    individual_day_number = str(individual_day)
    
    img = info[individual_day_number]['img']
    value = info[individual_day_number]['value']
    
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'bot', 'imgs', 'individual_days_numbers', img)
    with open(file_path, 'rb') as photo:
        file = types.InputFile(photo)
        await msg.answer_photo(photo=file, caption=value)
        keyboard = types.InlineKeyboardMarkup().add(back_to_base_forecast_button)
        await msg.answer('1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣\nК другим числам!', reply_markup=keyboard)
    await state.finish()
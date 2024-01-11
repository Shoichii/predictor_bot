from bot.loader import dp, bot
from aiogram import types
from bot.info.mind_numbers import message_text,get_mind_numbers_button , info
from bot.info.other_numbers import back_to_other_numbers_button
import asyncio
import bot.django_crud as dj
import os
from bot.prices import mind_number_price
from bot.utils import check_seals_amount


@dp.callback_query_handler(lambda call: call.data == 'mind_numbers_button')
async def open_mind_numbers(call: types.CallbackQuery):
    await call.message.delete()
    keyboard = types.InlineKeyboardMarkup().add(get_mind_numbers_button).add(back_to_other_numbers_button)
    await call.message.answer(message_text, reply_markup=keyboard, parse_mode='HTML')


@dp.callback_query_handler(lambda call: call.data == 'get_mind_numbers_button')
async def get_mind_numbers(call: types.CallbackQuery):
    await call.message.delete()
    is_seals_enough = await check_seals_amount(call.message, call.from_user.id, mind_number_price)
    if not is_seals_enough:
        return
    
    await dj.minus_seals(call.from_user.id, mind_number_price)
    user_data = await dj.get_user_data(call.from_user.id)
    name = user_data.name.split(' ')
    if len(name) == 1:
        name = name[0]
    else:
        name = name[1]
    birthday = user_data.birthday.strftime("%d.%m.%Y").split('.')[0]
    birthday = int(birthday)

    keyboard = types.InlineKeyboardMarkup().add(back_to_other_numbers_button)
    letters_list = [['А', 'И', 'С', 'Ъ',], ['Б', 'Й', 'Т', 'Ы',],['В', 'К', 'У', 'Ь',],['Г', 'Л', 'Ф', 'Э',],
                        ['Д', 'М', 'Х', 'Ю',],['Е', 'Н', 'Ц', 'Я',],['Ё', 'О', 'Ч'],['Ж', 'П', 'Ш'],
                        ['З', 'Р', 'Щ']]
        
    name_sum = 0
    for letter in name:
        for i, inside_list in enumerate(letters_list):
            if letter in inside_list:
                name_sum += i + 1
                break
        
    if name_sum != 11 or name_sum != 22 or name_sum != 33:
        while name_sum not in range(0,10):
            number_sum = 0
            for numb in str(name_sum):
                number_sum += int(numb)
            name_sum = number_sum
            
    mind_number = name_sum + birthday
    while mind_number not in range(0,10):
        number_sum = 0
        for numb in str(mind_number):
            number_sum += int(numb)
        mind_number = number_sum
    
    
    mind_number = str(mind_number)
    img = info[mind_number]['img']
    value = info[mind_number]['value']
    
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'bot', 'imgs', 'mind_numbers', img)
    with open(file_path, 'rb') as photo:
        file = types.InputFile(photo)
        await call.message.answer('👁👁👁Печати сорваны👁👁👁')
        await asyncio.sleep(0.3)
        await call.message.answer_photo(photo=file, caption=value)
        await call.message.answer('1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣\nК другим числам!', reply_markup=keyboard)
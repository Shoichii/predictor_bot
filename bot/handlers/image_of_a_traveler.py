from bot.loader import dp
from aiogram import types
from bot.info.other_numbers import back_to_other_numbers_button
import os

@dp.callback_query_handler(lambda call: call.data == 'image_of_a_traveler_button')
async def open_image_of_a_traveler(call: types.CallbackQuery):
    await call.message.delete()
    
    img = 'traveler.png'
    message = '''<b><u>Число жизненного пути</u></b> - это то, что далеко, но очень важно для Вас. То, к чему вы стремитесь, куда лежит Ваш путь. Это цель Вашего жизненного путешествия.

<b><u>Число душевного пробуждения</u></b> - это идея Вашего пути. То, зачем Вы стремитесь к своей цели. То желание, которое Вами движет.

<b><u>Число экспрессии</u></b> - как Вы сами видите, это всё то, что Вы взяли с собой в поход. Всё, что может пригодится. И рюкзак у каждого свой и по размеру и по весу.

<b><u>Число личности</u></b> - это Ваша одежда, весь Ваш внешний вид. Вы можете быть одеты красиво или надёжно для похода - по всякому. Это число - все Ваши вншние атрибуты.

<b><u>Число дня рождения</u></b> - это дорога/тропа по которой Вы идёте. Она может быть разной: извилистой, каменистой, поросшей травой, еле заметной или наоборот явно выделенной.

Один из способов понять общую картину, связав воедино все показатели нумерологического ядра - вообразить себе путника, идущего к своей цели.
Этот путник - это Вы  или любой другой человек, которого Вы хотели бы лучше узнать и понять, опираясь на нумерологию
'''
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'bot', 'imgs', 'image_of_a_traveler', img)
    with open(file_path, 'rb') as photo:
        file = types.InputFile(photo)
        keyboard = types.InlineKeyboardMarkup().add(back_to_other_numbers_button)
        await call.message.answer_photo(photo=file, caption=message,parse_mode='HTML', reply_markup=keyboard)
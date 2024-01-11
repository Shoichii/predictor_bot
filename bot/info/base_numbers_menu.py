from aiogram import types
from bot.info.main_numbs_menu import back_to_main_menu_button
import bot.django_crud as dj

# кнопка возврата в главное меню базовых чисел
back_to_base_numbers_button = types.InlineKeyboardButton('Назад', callback_data='back_to_base_numbers_button')

async def numb_core(msg: types.Message, telegram_id: int) -> None:
    seals_amount = await dj.get_seals_amount(telegram_id)
    message = f'''<b>Базовые, самые важные нумерологические характеристики человека заложены в этих числах.</b>

Узнав их, Вы увидите, что они могут быть совершенно разными. Как и сам человек проявляет себя совершенно по разному в разных ситуациях, местах и промежутках времени, так и числа, характеризующие его в том или ином виде выглядят по разному. Одно число говорит нам о нашей жизни в целом, другое - это наш инструмент в борьбе за нашу главную цель, третий - наша сущность в физическом мире и так далее. Откройте все свои базовые числа и Вы узнаете, что про Вас расскажет нумерология.

В Вашем распоряжении {seals_amount} 👁 печатей.
'''

    life_path_numbers_button = types.InlineKeyboardButton('Число жизненного пути', callback_data='life_path_numbers_button')
    birthday_numbers_button = types.InlineKeyboardButton('Число дня рождения', callback_data='birthday_numbers_button')
    expression_numbers_button = types.InlineKeyboardButton('Число экспрессии', callback_data='expression_numbers_button')
    spirit_awake_numbers_button = types.InlineKeyboardButton('Число душевного пробуждения', callback_data='spirit_awake_numbers_button')
    personality_numbers_button = types.InlineKeyboardButton('Число личности', callback_data='personality_numbers_button')

    base_numbers_keyboard = types.InlineKeyboardMarkup().add(life_path_numbers_button).add(birthday_numbers_button)\
        .add(expression_numbers_button).add(spirit_awake_numbers_button).add(personality_numbers_button).\
            add(back_to_main_menu_button)
    
    await msg.answer(message, reply_markup=base_numbers_keyboard)
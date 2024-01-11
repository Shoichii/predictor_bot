from aiogram import types
from bot.info.main_numbs_menu import back_to_main_menu_button
import bot.django_crud as dj

# кнопка возврата в главное меню базовых чисел
back_to_base_forecast_button = types.InlineKeyboardButton('Назад', callback_data='back_to_base_forecast_button')

async def forecast(msg: types.Message, telegram_id: int) -> None:
    seals_amount = await dj.get_seals_amount(telegram_id)
    message = f'''<b>Нумерологический прогноз</b> - этот прогноз не даст Вам точного описания того, что с Вами случится в то или иное время. Ровно как и не даст конкретных дат.
    Нумерологический прогноз это скорее подсказка какую энергию и в какой период жизни лучше использовать и какая тема в этот период будет более важной.
    Вы, конечно же, можете действовать как пожелаете. Это тоже самое, как встать рано утром и лечь спать обратно или пойти на работу. Выбор остаётся за Вами, но и последствия выбора будут соответствующие.
    
    В Вашем распоряжении {seals_amount} 👁 печатей.
    '''

    vertex_numbers_button = types.InlineKeyboardButton('Метод вершин', callback_data='vertex_numbers_button')
    test_numbers_button = types.InlineKeyboardButton('Испытания', callback_data='test_numbers_button')
    individual_years_numbers_button = types.InlineKeyboardButton('Индивидуальные годы', callback_data='individual_years_numbers_button')
    individual_months_numbers_button = types.InlineKeyboardButton('Индивидуальные месяцы', callback_data='individual_months_numbers_button')
    individual_days_numbers_button = types.InlineKeyboardButton('Индивидуальные дни', callback_data='individual_days_numbers_button')

    keyboard = types.InlineKeyboardMarkup().add(vertex_numbers_button)\
        .add(test_numbers_button).add(individual_years_numbers_button).add(individual_months_numbers_button)\
            .add(individual_days_numbers_button).add(back_to_main_menu_button)
    
    await msg.answer(message, reply_markup=keyboard)
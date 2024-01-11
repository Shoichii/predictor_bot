from aiogram import types
from bot.info.main_numbs_menu import back_to_main_menu_button
import bot.django_crud as dj

# кнопка возврата в главное меню базовых чисел
back_to_other_numbers_button = types.InlineKeyboardButton('Назад', callback_data='back_to_other_numbers_button')

async def core_synthez(msg: types.Message, telegram_id: int) -> None:
    seals_amount = await dj.get_seals_amount(telegram_id)
    message = f'''<b>Синтез нумерологического ядра это способы понять и связать между собой базовые нумерологические характеристики из раздела "нумерологическое ядро".</b>
    Получив 5 разных(порой схожих) чисел нам теперь нужно как то их связать и получить общую картину о конкретном человеке. Каждое число имеет свою роль и своё место в жизни человека, а сам человек действует, мыслит и ведёт себя по разному в различных ситуациях и промежутках времени.
    Именно для этого и нужен синтез ядра - набор способов и методов составления единого целого из разрозненных осколков.
    
    В Вашем распоряжении {seals_amount} 👁 печатей.
    '''

    image_of_a_traveler_button = types.InlineKeyboardButton('Образ путника', callback_data='image_of_a_traveler_button')
    realization_numbers_button = types.InlineKeyboardButton('Число реализации', callback_data='realization_numbers_button')
    bridges_numbers_button = types.InlineKeyboardButton('Числа-мосты', callback_data='bridges_numbers_button')
    mind_numbers_button = types.InlineKeyboardButton('Число разума', callback_data='mind_numbers_button')

    other_numbers_keyboard = types.InlineKeyboardMarkup().add(image_of_a_traveler_button)\
        .add(realization_numbers_button).add(bridges_numbers_button).add(mind_numbers_button).add(back_to_main_menu_button)
    
    await msg.answer(message, reply_markup=other_numbers_keyboard)
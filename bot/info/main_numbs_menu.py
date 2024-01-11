from aiogram import types
import bot.django_crud as dj

# кнопка 🔮 Нумерология
async def numerology_button(msg: types.Message, telegram_id: int) -> None:
    seals_amount = await dj.get_seals_amount(telegram_id)
    message = f'''<b>🔮Нумерология🔮</b>

Здесь Вы можете использовать знания нумерологии, чтобы лучше узнать себя, понять своих близких, узнать о совместимостях и исследовать любого человека с помощью чисел.

Но помните, что нумерология это только рекомендации и ознакомительная информация. Прежде всего Вы сами вольны выбирать свой путь. У каждого человека имеется своя воля и свой характер.

В Вашем распоряжении {seals_amount} 👁 печатей.
'''
    base_numbers = types.InlineKeyboardButton('Нумерологическое ядро', callback_data='base_numbers_main_menu')
    other_numbers = types.InlineKeyboardButton('Синтез ядра', callback_data='other_numbers_main_menu')
    forecast_numbers = types.InlineKeyboardButton('Прогноз', callback_data='forecast_numbers_main_menu')
    relationship_button = types.InlineKeyboardButton('Взаимоотношения', callback_data='relationship_button_main_menu')
    main_numbs_menu_keyboard = types.InlineKeyboardMarkup().add(base_numbers).add(other_numbers)\
    .add(forecast_numbers).add(relationship_button)
    await msg.answer(message, reply_markup=main_numbs_menu_keyboard)

# кнопки возврата в главное меню нумерологии
back_to_main_menu_button = types.InlineKeyboardButton('Назад', callback_data='back_to_main_menu_button')

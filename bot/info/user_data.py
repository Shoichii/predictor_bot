from aiogram import types
import bot.django_crud as dj
from datetime import datetime

async def data_button(msg: types.Message, user_id: int) -> None:
    user_data = await dj.get_user_data(user_id)
    birthday = datetime.strftime(user_data.birthday, "%d.%m.%Y")
    message = f'''Текущие данные:
ФИО: <b>{user_data.name}</b>
День рождения: <b>{birthday}</b>

Количество печатей: {user_data.seals}

При изменении ФИО или даты рождения старые результаты будут сброшены!
(Но они сохраняться у Вас среди сообщений❤️)
Что желаете изменить?
'''
    change_name_button = types.InlineKeyboardButton('ФИО', callback_data='change_name_button')
    change_birthday_button = types.InlineKeyboardButton('Дату рождения', callback_data='change_birthday_button')
    keyboard = types.InlineKeyboardMarkup().add(change_name_button).add(change_birthday_button)
    await msg.answer(message,reply_markup=keyboard)


cancel_change_data_button = types.InlineKeyboardButton('Отмена', callback_data='cancel_change_data_button')
keyboard = types.InlineKeyboardMarkup().add(cancel_change_data_button)
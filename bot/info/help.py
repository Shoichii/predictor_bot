from aiogram import types

async def show_help_information(msg: types.Message) -> None:
    telegram_id = msg.from_user.id
    message = f'''Задать интересующие вопросы и получить помощь можно, 
написав нам на email.
Обязательно укажите Ваш ID в письме, чтобы мы могли Вас 
идентифировать.
email: <code>predictor-support@ro.ru</code>
ID: <code>{telegram_id}</code>
(Нажмите на email и ID, чтобы скопировать их)
'''
    await msg.answer(message)
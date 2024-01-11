from bot.loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import bot.django_crud as dj
from bot.info.main_numbs_menu import back_to_main_menu_button
from numerologist.settings import ADM_IDS

@dp.message_handler(content_types=['text'])
async def common(msg: types.Message, state=FSMContext):
    was_consultation_purchased = await dj.check_consultation_buy(msg.from_user.id)
    if was_consultation_purchased:
        await state.update_data(question=msg.text)
        message = 'Вопрос принят! Вы можете отправить свой вопрос нумерологу, нажав на кнопку ниже.'
        message += 'Если перед отправкой Вы решили изменить свой вопрос, то просто пришлите мне другое сообщение.'
        send_question_button = types.InlineKeyboardButton('Отправить', callback_data='send_question_button')
        keyboard = types.InlineKeyboardMarkup().add(send_question_button)
        await msg.answer(message, reply_markup=keyboard)


@dp.callback_query_handler(lambda call: call.data == 'send_question_button')
async def send_question(call: types.CallbackQuery, state=FSMContext):
    state_data = await state.get_data()
    question = state_data.get('question')
    message = f'''
Пользователь с id <b>{call.from_user.id}</b> прислал(а) вопрос:

{question}
'''
    await call.message.delete()
    await dj.set_question(call.from_user.id, question)
    adm_ids = ADM_IDS.split(',')
    for adm in adm_ids:
        await bot.send_message(int(adm), message, parse_mode='HTML')
    client_message = 'Ваш вопрос был отправлен нумерологу. Ожидая ответа можете посчитать числа знакомого Вам человека или знаменитости.'
    keyboard = types.InlineKeyboardMarkup().add(back_to_main_menu_button)
    await call.message.answer(client_message, reply_markup=keyboard)
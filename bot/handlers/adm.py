from aiogram import types
from bot.loader import dp,bot
from aiogram.dispatcher import FSMContext
from bot.states import Adm
from numerologist.settings import ADM_IDS
from bot.info.adm import show_adm_menu
import bot.django_crud as dj

@dp.message_handler(commands=['adm'])
async def open_adm_panel(msg: types.Message):
    if str(msg.from_user.id) in ADM_IDS:
        statistic = await dj.get_all_statistic()
        await show_adm_menu(statistic, msg)


@dp.callback_query_handler(lambda call: call.data == 'speaker_button')
async def speaker(call: types.CallbackQuery):
    await call.message.delete()
    cancel_megaphone_button = types.InlineKeyboardButton(text='Отмена', callback_data='cancel_megaphone_button')
    keyboard = types.InlineKeyboardMarkup().add(cancel_megaphone_button)
    await call.message.answer('Напишите одно сообщение, которое будет отправлено всем пользователям.\nМожно добавить одно фото.',
                            reply_markup=keyboard)
    await Adm.message_for_all.set()


@dp.callback_query_handler(lambda call: call.data == 'cancel_megaphone_button', state=Adm.message_for_all)
async def cancel_megaphone(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('Рассылка отменена')
    await state.finish()


@dp.message_handler(state=Adm.message_for_all, content_types=['text','photo'])
async def speaker_message(msg: types.Message, state: FSMContext):
    if msg.photo:
        if msg.caption:
            await state.update_data(text_for_all=msg.caption, photo_for_all=msg.photo[-1].file_id)
        else:
            await state.update_data(photo_for_all=msg.photo[-1].file_id)
    else:
        await state.update_data(text_for_all=msg.text)
    
    cancel_megaphone_button = types.InlineKeyboardButton(text='Отмена', callback_data='cancel_megaphone_button')
    send_megaphone_button = types.InlineKeyboardButton(text='Отправить', callback_data='send_megaphone_button')
    keyboard = types.InlineKeyboardMarkup().row(send_megaphone_button, cancel_megaphone_button)

    await msg.answer('Отправить?', reply_markup=keyboard)


@dp.callback_query_handler(lambda call: call.data == 'send_megaphone_button', state=Adm.message_for_all)
async def send_megaphone(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    state_data = await state.get_data()

    users_ids = await dj.get_all_users_id()

    if not users_ids:
        await call.message.answer('Нет пользователей')
        await state.finish()
        return

    photo = state_data.get('photo_for_all')
    text = state_data.get('text_for_all')
    if photo:
        if text:
            for id in users_ids:
                await bot.send_photo(chat_id=id, photo=photo, caption=text)
        else:
            for id in users_ids:
                await bot.send_photo(chat_id=id, photo=photo)
    else:
        for id in users_ids:
            await bot.send_message(chat_id=id, text=text)
    await call.message.answer('Оповещение успешно отправлено')
    await state.finish()

    
    
@dp.callback_query_handler(lambda call: call.data == 'add_or_del_seals_button')
async def add_or_del_seals(call: types.CallbackQuery):
    await call.message.delete()
    seals_add_button = types.InlineKeyboardButton('Прибавить', callback_data='seals_add_button')
    seals_del_button = types.InlineKeyboardButton('Отнять', callback_data='seals_del_button')
    keyboard = types.InlineKeyboardMarkup().row(seals_add_button, seals_del_button)
    await call.message.answer('Выбери действие', reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data == 'cancel_seals_button', state=Adm.seals_action)
async def cancel_seals(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.answer()
    await call.message.answer('Действие отменено')
    await state.finish()

@dp.callback_query_handler(lambda call: call.data == 'seals_add_button' or call.data == 'seals_del_button')
async def select_consult_action(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    action = call.data.split('_')[1]
    await state.update_data(seals_action=action)
    cancel_seals_button = types.InlineKeyboardButton('Отмена', callback_data='cancel_seals_button')
    keyboard = types.InlineKeyboardMarkup().add(cancel_seals_button)
    await call.message.answer('Теперь напиши id пользователя', reply_markup=keyboard)
    await Adm.seals_action.set()
    
@dp.message_handler(state=Adm.seals_action)
async def get_number(msg: types.Message, state: FSMContext):
    if not msg.text.isdigit():
        await msg.answer('Вводи только число')
        return
    else:
        is_user_exists = await dj.check_user_exists(int(msg.text))
        if not is_user_exists:
            statistic = await dj.get_all_statistic()
            await show_adm_menu(statistic, msg)
            await state.finish()
            await msg.answer('Пользователь с таким ID не найден. Возможно ID был введён неверно.')
            return
    await state.update_data(user_id=msg.text)
    cancel_seals_button = types.InlineKeyboardButton('Отмена', callback_data='cancel_seals_button')
    keyboard = types.InlineKeyboardMarkup().add(cancel_seals_button)
    await msg.answer('Теперь введи количество печатей', reply_markup=keyboard)
    await Adm.user_id.set()

@dp.callback_query_handler(lambda call: call.data == 'cancel_seals_button', state=Adm.user_id)
async def cancel_seals(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('Действие отменено')
    await state.finish()

@dp.message_handler(state=Adm.user_id)
async def get_number(msg: types.Message, state: FSMContext):
    if not msg.text.isdigit():
        await msg.answer('Вводи только число')
        return
    state_data =await state.get_data()
    action = state_data.get('seals_action')
    user_id = state_data.get('user_id')
    statistic = await dj.get_all_statistic()
    await dj.set_seals(user_id,int(msg.text),action=action)
    await show_adm_menu(statistic, msg)
    await msg.answer('Действие выполнено')
    await state.finish()

##################################################
# @dp.callback_query_handler(lambda call: call.data and call.data.startswith('answer_button'))
# async def start_answer(call: types.CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     _, id = call.data.split(':')
#     await state.update_data(user_id=id)
#     cancel_answer_button = types.InlineKeyboardButton('Отменить', callback_data='cancel_answer_button')
#     keyboard = types.InlineKeyboardMarkup().add(cancel_answer_button)
#     user = await db.get_user(id)
#     numbers = user.all_numbers.split(',')
#     life_path_number = numbers[0]
#     birthday_number = numbers[1]
#     expression_number = numbers[2]
#     spirit_awake_number = numbers[3]
#     personality_number = numbers[4]
    
#     await call.message.answer(f'''Напишите текст для отправка клиенту.

# Данные клиента:
# Имя: {user.name}
# День рождения: {user.birthday}
# Число жизненного пути: {life_path_number}
# Число дня рождения: {birthday_number}
# Число экспрессии: {expression_number}
# Число духовного пробуждения: {spirit_awake_number}
# Число личности: {personality_number}

# По желанию можно прикрепить 1 фото.''', reply_markup=keyboard)
#     await Adm.answer.set()

# @dp.callback_query_handler(lambda call: call.data == 'cancel_answer_button', state=Adm.answer)
# async def cancel_answer(call: types.CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     state_data = await state.get_data()
#     user_id = state_data.get('user_id')
#     await db.drop_answer(user_id)
#     await call.message.answer('Отправка ответа отменена.')
#     await state.finish()

# @dp.message_handler(state=Adm.answer, content_types=['text', 'photo'])
# async def take_answer(msg: types.Message, state: FSMContext):
#     if msg.content_type != 'text' and msg.content_type != 'photo':
#         await msg.answer('Отправка такого типа контента не предусмотрена.')
#         return
#     state_data = await state.get_data()
#     user_id = state_data.get('user_id')
#     if msg.content_type == 'text':
#         await db.set_answer(user_id, msg.text, False)
#     if msg.content_type == 'photo':
#         await db.set_answer(user_id, msg.caption, True)
#         await db.set_pic_answer(user_id, msg.photo[-1].file_id)
#     is_send_button = types.InlineKeyboardButton('Отправить', callback_data='is_send_button')
#     cancel_answer_button = types.InlineKeyboardButton('Отменить', callback_data='cancel_answer_button')
#     keyboard = types.InlineKeyboardMarkup().row(cancel_answer_button, is_send_button)
#     await msg.answer('Если желаете дополнить, то просто напишите ещё. В ином случае выберите отправить или отменить.',
#                     reply_markup=keyboard)

# @dp.callback_query_handler(lambda call: call.data == 'is_send_button', state=Adm.answer)
# async def send_message(call: types.CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     state_data = await state.get_data()
#     user_id = state_data.get('user_id')
#     answer = await db.get_answer(user_id)
#     answer_text = answer.get('answer')
#     if answer_text:
#         answer_text = answer_text.split('\n')
#         for message in answer_text:
#             if 'for_photo' in message:
#                 caption = message.replace('for_photo', '')
#                 await bot.send_photo(chat_id=user_id, photo=answer.get('photo'), caption=caption)
#             else:
#                 await bot.send_message(chat_id=user_id, text=message)
#     else:
#         await bot.send_photo(chat_id=user_id, photo=answer.get('photo'))
#     await db.set_was_answer(user_id, True)
#     await db.set_question_was_send(user_id, False)
#     await db_statistic.set_personal_consultation()
#     await db.drop_buy_consultation(user_id)
#     await call.message.answer('Ответ отправлен.')
#     await state.finish()
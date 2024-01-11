from aiogram import types
from bot.loader import dp
import bot.info.numerology_relationship as nr

#душевное пробуждение совпадает с одним из чисел нумерологического ядра
@dp.callback_query_handler(lambda call: call.data == 'spirit_awake_num_button')
async def spirit_awake_num(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(nr.spirit_awake_message, reply_markup=nr.spirit_awake_keyboard, parse_mode='HTML')
    
@dp.callback_query_handler(lambda call: call.data == 'spirit_awake_with_spirit_awake_button' or 
    call.data == 'spirit_awake_with_personality_button' or call.data == 'spirit_awake_with_expression_button' or
    call.data == 'spirit_awake_with_life_path_button' or call.data == 'spirit_awake_with_birthday_button')
async def spirit_awake_with_spirit_awake(call: types.CallbackQuery):
    await call.message.delete()
    data = call.data
    button = types.InlineKeyboardButton('Назад', callback_data='spirit_awake_num_button')
    keyboard = types.InlineKeyboardMarkup().add(button)
    if data == 'spirit_awake_with_spirit_awake_button':
        await call.message.answer(nr.spirit_awake_with_spirit_awake_message, reply_markup=keyboard)
    if data == 'spirit_awake_with_personality_button':
        await call.message.answer(nr.spirit_awake_with_personality_message, reply_markup=keyboard)
    if data == 'spirit_awake_with_expression_button':
        await call.message.answer(nr.spirit_awake_with_expression_message, reply_markup=keyboard)
    if data == 'spirit_awake_with_life_path_button':
        await call.message.answer(nr.spirit_awake_with_life_path_message, reply_markup=keyboard)
    if data == 'spirit_awake_with_birthday_button':
        await call.message.answer(nr.spirit_awake_with_birthday_message, reply_markup=keyboard)

#экспрессия совпадает с одним из чисел нумерологического ядра
@dp.callback_query_handler(lambda call: call.data == 'expression_num_button')
async def expression_num(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(nr.expression_message, reply_markup=nr.expression_keyboard, parse_mode='HTML')
    
@dp.callback_query_handler(lambda call: call.data == 'expression_with_personality_button' or 
    call.data == 'expression_with_expression_button' or
    call.data == 'expression_with_life_path_button' or call.data == 'expression_with_birthday_button')
async def expression_with_expression(call: types.CallbackQuery):
    await call.message.delete()
    data = call.data
    button = types.InlineKeyboardButton('Назад', callback_data='expression_num_button')
    keyboard = types.InlineKeyboardMarkup().add(button)
    if data == 'expression_with_personality_button':
        await call.message.answer(nr.expression_with_personality_message, reply_markup=keyboard)
    if data == 'expression_with_expression_button':
        await call.message.answer(nr.expression_with_expression_message, reply_markup=keyboard)
    if data == 'expression_with_life_path_button':
        await call.message.answer(nr.expression_with_life_path_message, reply_markup=keyboard)
    if data == 'expression_with_birthday_button':
        await call.message.answer(nr.expression_with_birthday_message, reply_markup=keyboard)

#другие совпадения
@dp.callback_query_handler(lambda call: call.data == 'other_num_button')
async def expression_num(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(nr.other_message, reply_markup=nr.other_keyboard, parse_mode='HTML')
    
@dp.callback_query_handler(lambda call: call.data == 'life_path_with_life_path_button' or 
    call.data == 'life_path_with_birthday_button' or
    call.data == 'life_path_birthday_with_personality_button' or call.data == 'personality_with_personality_button')
async def other_with_other(call: types.CallbackQuery):
    await call.message.delete()
    data = call.data
    button = types.InlineKeyboardButton('Назад', callback_data='other_num_button')
    keyboard = types.InlineKeyboardMarkup().add(button)
    if data == 'life_path_with_life_path_button':
        await call.message.answer(nr.life_path_with_life_path_message, reply_markup=keyboard)
    if data == 'life_path_with_birthday_button':
        await call.message.answer(nr.life_path_with_birthday_message, reply_markup=keyboard)
    if data == 'life_path_birthday_with_personality_button':
        await call.message.answer(nr.life_path_birthday_with_personality_message, reply_markup=keyboard)
    if data == 'personality_with_personality_button':
        await call.message.answer(nr.personality_with_personality_message, reply_markup=keyboard)

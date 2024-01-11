from bot.info.main_numbs_menu import numerology_button
from bot.info.help import show_help_information
from bot.info.user_data import data_button
from aiogram import types
import bot.django_crud as dj
from bot.info.main_numbs_menu import back_to_main_menu_button


# кнопки главного
main_buttons = ['🪄 Магазин', '🔮 Нумерология', '🆘 Помощь', '📄 Данные']

# рандомное сообщение для зарегистрированных пользователей при вызове команды /start
random_message = ['М?', 'Вы уже зарегистрированы. Справка на кнопке "🆘 Помощь"', 
                'Если у Вас пропала клавиатура внизу, то найдите внизу кнопку с 4мя квадратиками.',
                'Я могу быть долго Вам полезен, если Вы знаете, что хотите)))',
                'На Ваши донаты я готов становится лучше.',
                'Спасибо, что поддерживаете меня!']


async def execute_main_commands(msg: types.Message, command: str) -> None:

    match command:
        case '🔮 Нумерология':
            await numerology_button(msg, msg.from_user.id)
        case '🆘 Помощь':
            await show_help_information(msg)
        case '📄 Данные': 
            await data_button(msg, msg.from_user.id)


# стикер загрузки
sticker = 'CAACAgIAAxkBAAEIoqhkP8DGER8rvuJzsCx4YDp-EiVDYQACdFsBAAFji0YM3S9lzUKXpDgvBA'

async def check_seals_amount(msg, telegram_id, price):
    seals_amount = await dj.get_seals_amount(telegram_id)
    if seals_amount - price < 0:
        keyboard = types.InlineKeyboardMarkup().add(back_to_main_menu_button)
        await msg.answer('''К сожалению у Вас недостаточно печатей для этих знаний. 
Вы можете получить ещё в магазине.''', reply_markup=keyboard)
        return False
    return True


async def add_base_numbers_to_msg(message, base_numbers):
    message += '<b>Ваши базовые числа(нумерологическое ядро) :</b>\n\n'
    count = 0
    if not base_numbers.life_path_number:
        life_path = 'Неизвестно'
    else:
        life_path = base_numbers.life_path_number
    message += f'Число жизненного пути - <b>{life_path}</b>\n'
    if not base_numbers.birthday_number:
        birthday = 'Неизвестно'
    else:
        birthday = base_numbers.birthday_number
    message += f'Число дня рождения - <b>{birthday}</b>\n'
    if not base_numbers.expression_number:
        expression = 'Неизвестно'
    else:
        expression = base_numbers.expression_number
    message += f'Число экспрессии - <b>{expression}</b>\n'
    if not base_numbers.spirit_awake_number:
        spirit_awake = 'Неизвестно'
    else:
        spirit_awake = base_numbers.spirit_awake_number
    message += f'Число душевного пробуждения - <b>{spirit_awake}</b>\n'
    if not base_numbers.personality_number:
        personality = 'Неизвестно'
    else:
        personality = base_numbers.personality_number
    message += f'Число личности - <b>{personality}</b>\n'

    return {
        'message': message,
        'count': count
    }